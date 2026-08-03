class Solution:
    # Brute Force
    # Runtime: Time Limit Exceeded
    # Memory: Time Limit Exceeded
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def characterReplacement(self, s: str, k: int) -> int:
        longest_substring = 0

        for i in range(len(s)):
            char_count = {}
            max_frequency = 0

            for j in range(i, len(s)):
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

        return longest_substring