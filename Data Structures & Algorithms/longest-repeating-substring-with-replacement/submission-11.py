class Solution:
    # Sliding Window Approach
    # Runtime: 64ms
    # Memory: 8.5 MB
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def characterReplacement(self, s: str, k: int) -> int:
        longest_substring = 0
        char_count = {}
        max_frequency = 0
        i = 0
        j = 0

        while j < len(s):
            char_j = s[j]

            if char_j in char_count:
                char_count[char_j] += 1
            else:
                char_count[char_j] = 1
            
            char_j_count = char_count[char_j]

            if char_j_count > max_frequency:
                max_frequency = char_j_count

            window_size = j - i + 1
            replacement_count = window_size - max_frequency

            if replacement_count <= k:
                longest_substring = max(longest_substring, window_size)
                j += 1
            else:
                char_i = s[i]
                char_count[char_i] -= 1
                max_frequency = max(char_count.values())
                i += 1
                j += 1

        return longest_substring