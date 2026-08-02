class Solution:
    # Brute Force
    # Runtime: Time Limit Exceeded
    # Memory: Time Limit Exceeded
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring_length = 0

        for i in range(len(s)):
            current_substring = {s[i]}
            current_substring_length = 1

            for j in range(i + 1, len(s)):
                char = s[j]
                if char in current_substring:
                    break
                else:
                    current_substring.add(char)
                    current_substring_length += 1
            
            if current_substring_length > longest_substring_length:
                longest_substring_length = current_substring_length

        return longest_substring_length