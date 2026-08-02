class Solution:
    # Sliding Window
    # Runtime: 134ms
    # Memory: 8.8 MB
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_substring = set()
        longest_substring_length = 0
        l = 0
        r = 0

        while r < len(s):
            char_l = s[l]
            char_r = s[r]

            if char_r in current_substring:
                current_substring_length = r - l
                current_substring.remove(s[l])
                l += 1
                
                if current_substring_length > longest_substring_length:
                    longest_substring_length = current_substring_length
            else:
                current_substring_length = r - l + 1
                current_substring.add(char_r)
                r += 1

                if current_substring_length > longest_substring_length:
                    longest_substring_length = current_substring_length
        
        return longest_substring_length