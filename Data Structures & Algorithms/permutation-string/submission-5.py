class Solution:
    # Sliding Window Approach
    # Runtime: 45ms
    # Memory: 7.9 MB
    # Time Complexity: O(nm)
    # Space Complexity: O(nm)
    # n is the length of s2
    # m is the length of s1
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_char_count = {}
        s1_char_hash_set = set(s1)

        for s1_char in s1:
            if s1_char in s1_char_count:
                s1_char_count[s1_char] += 1
            else:
                s1_char_count[s1_char] = 1
        
        i = 0
        j = 0
        s2_window_char_count = {}
        
        while j < len(s2):
            char_i = s2[i]
            char_j = s2[j]

            if char_j in s2_window_char_count:
                s2_window_char_count[char_j] += 1
            else:
                s2_window_char_count[char_j] = 1
            
            if s2_window_char_count == s1_char_count:
                return True
            elif char_j not in s1_char_hash_set:
                i = j + 1
                j = i
                s2_window_char_count = {}
            elif s2_window_char_count[char_j] > s1_char_count[char_j]:
                i += 1
                j += 1
                s2_window_char_count[char_i] -= 1
            else:
                j += 1
        
        return False