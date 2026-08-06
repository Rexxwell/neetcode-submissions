class Solution:
    # Brute Force
    # Runtime: TLE
    # Memory: TLE
    # Time Complexity: O(n^2m)
    # Space Complexity: O(n)
    # n is the length of s.
    # m is the length of t.
    def minWindow(self, s: str, t: str) -> str:
        shortest_substring_len = float('inf')
        shortest_substring_start = 0
        shortest_substring_end = 0

        if len(s) < len(t):
            return s[shortest_substring_start:shortest_substring_end]
        
        t_char_count = {}

        for t_char in t:
            if t_char in t_char_count:
                t_char_count[t_char] += 1
            else:
                t_char_count[t_char] = 1

        for i in range(len(s)):
            s_char_count = {}

            for j in range(i, len(s)):
                char_j = s[j]

                if char_j in s_char_count:
                    s_char_count[char_j] += 1
                else:
                    s_char_count[char_j] = 1

                is_valid = all(t_key in s_char_count and s_char_count[t_key] >= t_value for t_key, t_value in t_char_count.items())
                
                if is_valid:
                    substring_len = j - i + 1

                    if substring_len < shortest_substring_len:
                        shortest_substring_len = substring_len
                        shortest_substring_start = i
                        shortest_substring_end = j + 1

                    break

        return s[shortest_substring_start:shortest_substring_end]