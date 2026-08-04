class Solution:
    # Brute Force
    # Runtime: 74ms
    # Memory: 7.7 MB
    # Time Complexity: O(nm^2)
    # Space Complexity: O(n + m)
    # n is the length of s1.
    # m is the length of s2.
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_char_count = {}
        s1_char_hash = set(s1)

        for s1_char in s1:
            if s1_char in s1_char_count:
                s1_char_count[s1_char] += 1
            else:
                s1_char_count[s1_char] = 1
        
        for i in range(len(s2)):
            s2_char_count = {}

            for j in range(i, len(s2)):
                s2_char_j = s2[j]

                if s2_char_j in s2_char_count:
                    s2_char_count[s2_char_j] += 1
                else:
                    s2_char_count[s2_char_j] = 1
                
                if s2_char_count == s1_char_count:
                    return True

        return False