import operator

class Solution:
    # Brute Force
    # Runtime: TLE
    # Memory: TLE
    # Time Complexity: O(n^2)
    # Space Complexity: O(1) auxillary space, O(n) implementation overhead
    def evalRPN(self, tokens: List[str]) -> int:
        i = 0

        while i < len(tokens):
            token = tokens[i]

            if token in "+-*/":
                operand_1 = int(tokens[i - 2])
                operand_2 = int(tokens[i - 1])
                result = 0

                if token == "+":
                    result = operand_1 + operand_2
                elif token == "-":
                    result = operand_1 - operand_2
                elif token == "*":
                    result = operand_1 * operand_2
                elif token == "/":
                    result = int(operand_1 / operand_2)
                
                tokens[i - 2: i + 1] = [str(result)]
                i = 0
            else:
                i += 1
        
        return int(tokens[0])