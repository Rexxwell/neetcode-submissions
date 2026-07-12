class Solution:
    # Dictionary
    # Runtime: 52ms
    # Memory: 8.5 MB
    # Time Complexity: O(nklogk)
    # Space Complexity: O(nk)
    #   where n is the length of the `strs` List
    #   k is the maximum length of a string in the input list.
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_list = []
        anagram_dict = {}
        for string in strs:
            sorted_characters = sorted(string)
            sorted_string = "".join(sorted_characters)
            if sorted_string in anagram_dict:
                anagram_dict[sorted_string].append(string)
            else:
                anagram_dict[sorted_string] = [string]

        for value in anagram_dict.values():
            anagram_list.append(value)

        return anagram_list 