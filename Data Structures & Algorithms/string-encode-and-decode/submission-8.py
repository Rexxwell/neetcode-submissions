class Solution:
    # One pointer and one length variable
    # Runtime: 52ms
    # Memory: 8.2 MB
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        
        for string in strs:
            encoded_string += f"{len(string)}#{string}"

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        current_string_length = 0
        current_string_pointer = 0

        while current_string_pointer < len(s):
            string_length = ""

            for character in s[current_string_pointer:]:
                if character == "#":
                    break
                else:
                    string_length += character
            
            current_string_length = int(string_length)

            if current_string_length == 0:
                decoded_strs.append("")
                current_string_length = 0
                current_string_pointer += 2
                continue

            current_string_pointer += len(string_length) + 1
            current_string = ""

            for i in range(current_string_pointer, current_string_pointer + current_string_length):
                current_string += s[i]
            
            decoded_strs.append(current_string)
            current_string_pointer += current_string_length
        
        return decoded_strs