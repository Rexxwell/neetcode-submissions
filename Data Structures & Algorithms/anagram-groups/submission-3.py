class Solution:
    # Character Count
    # Runtime: 51ms
    # Memory: 8.5 MB
    # Time Complexity: O(nk)
    # Space Complexity: O(nk)
    #   where n is the length of the strs list
    #   k is the maximum length of the string in the strs list.
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        anagram_list = []
        for string in strs:
            character_count = [0] * 26
            for character in string:
                character_count[ord(character) - 97] += 1
            
            character_count_tuple = tuple(character_count)
            if (character_count_tuple in anagram_dict):
                anagram_dict[character_count_tuple].append(string)
            else:
                anagram_dict[character_count_tuple] = [string]
        
        for value in anagram_dict.values():
            anagram_list.append(value)
        
        return anagram_list