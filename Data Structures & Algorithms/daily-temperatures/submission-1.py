class Solution:
    # Brute Force
    # Runtime: TLE
    # Memory: TLE
    # Time Complexity: O(n^2)
    # Space Complexity: O(1) auxillary space, O(n)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []

        for i in range(len(temperatures)):
            current_temperature = temperatures[i]
            days = 1
            has_warmer_temperature = False

            for j in range(i + 1, len(temperatures)):
                temperature = temperatures[j]

                if temperature > current_temperature:
                    has_warmer_temperature = True
                    break
                
                days += 1
            
            if has_warmer_temperature:
                result.append(days)
            else:
                result.append(0)
        
        return result
                