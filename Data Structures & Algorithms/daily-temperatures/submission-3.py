class Solution:
    # Stack
    # Runtime: 127ms
    # Memory: 10.9 MB
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # Time complexity is O(n) because the inner while loop runs a maximum of n times since
    # we never re-add elements into the stack, we only pop a maximum of n times throughout
    # the entire outer for loop. Thus, O(n) for loop + O(n) pops = O(n).
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        if len(temperatures) == 0:
            return result
        
        stack = []
        stack.append(0)

        for i in range(1, len(temperatures)):
            temperature = temperatures[i]
            stack_top_temperature = temperatures[stack[-1]]
            
            if temperature <= stack_top_temperature:
                stack.append(i)
            else:
                while len(stack) != 0:
                    stack_top_temperature = temperatures[stack[-1]]
                    
                    if stack_top_temperature < temperature:
                        stack_top_index = stack.pop()
                        result[stack_top_index] = i - stack_top_index
                    else:
                        break
                
                stack.append(i)

        return result