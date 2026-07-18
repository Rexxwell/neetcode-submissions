class Solution:
    # Length prefixing V2
    # Runtime: 31ms
    # Memory: 8.5 MB
    # Time Complexity: O(n)
    # Space Complexity: O(n)

    def encode(self, strs: List[str]) -> str:
        encoded_string = []
        
        for string in strs:
            encoded_string.append(f"{len(string)}#{string}")

        return "".join(encoded_string)
        
    def decode(self, s: str) -> List[str]:
        print(s)
        decoded_strs = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            len_str = int(s[i:j])
            i = j + 1
            decoded_strs.append(s[i:i + len_str])
            i += len_str
        
        return decoded_strs