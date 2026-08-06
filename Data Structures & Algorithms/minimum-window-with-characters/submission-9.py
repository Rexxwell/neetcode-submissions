class Solution:
    # Sliding Window Approach
    # Runtime: 62ms
    # Memory: 8.4 MB
    # Time Complexity: O(|s| + |t|)
    # Space Complexity: O(52)
    # Since s and t consist of uppercase and lowercase English letters.
    # The maximum number of key-value pairs t_char_count and window_char_count
    # can have is 52.
    # 
    # The time complexity of the for while loop is O(|s|) because the inner while
    # loop runs and increments i but does not reset i. Thus, it is an amortized
    # O(|s|). So, the inner while loop will run an maximum of O(|s| - |t|)
    # throughout the entire outer for loop.
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        t_char_count = {}

        for t_char in t:
            if t_char in t_char_count:
                t_char_count[t_char] += 1
            else:
                t_char_count[t_char] = 1
        
        window_char_count = {}
        shortest_substring_length = float('inf')
        shortest_substring_start_index = 0
        shortest_substring_end_index = 0
        need = len(t_char_count)
        have = 0
        i = 0

        for j in range(len(s)):
            s_char_j = s[j]
            window_char_count[s_char_j] = window_char_count.get(s_char_j, 0) + 1

            if s_char_j in t_char_count and window_char_count[s_char_j] == t_char_count[s_char_j]:
                have += 1
            
            while have == need:
                window_length = j - i + 1

                if window_length < shortest_substring_length:
                    shortest_substring_length = window_length
                    shortest_substring_start_index = i
                    shortest_substring_end_index = j

                s_char_i = s[i]
                window_char_count[s_char_i] -= 1

                if s_char_i in t_char_count and window_char_count[s_char_i] < t_char_count[s_char_i]:
                    have -= 1
                
                i += 1
        
        return s[shortest_substring_start_index:shortest_substring_end_index + 1] if shortest_substring_length != float('inf') else ""