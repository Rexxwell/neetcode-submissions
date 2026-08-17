class TimeMap:
    # Binary Search
    # Runtime: 561ms
    # Memory: 15.9 MB
    # Time Complexity: O(logn)
    # Space Complexity: O(n)
    # n is the length of the input

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map:
            self.time_map[key].append((value, timestamp))
        else:
            self.time_map[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.time_map:
            low = 0
            high = len(self.time_map[key]) - 1
            result = -1

            while low <= high:
                mid = low + (high - low) // 2
                value, timestamp_prev = self.time_map[key][mid]

                if timestamp_prev == timestamp:
                    return value
                elif timestamp_prev > timestamp:
                    high = mid - 1
                elif timestamp_prev < timestamp:
                    result = mid
                    low = mid + 1

            return "" if result == -1 else self.time_map[key][result][0]
        else:
            return ""