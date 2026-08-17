class TimeMap:
    # Brute Force
    # Runtime: 2592ms
    # Memory: 15.7 MB
    # Time Complexity: O(n)
    # Space Complexity: O(n)

    def __init__(self):
        self.time_map = []

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map.append((key, value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        largest_value = ""
        largest_timestamp = 0

        for key_prev, value, timestamp_prev in self.time_map:
            if key_prev == key and timestamp_prev <= timestamp and timestamp_prev >= largest_timestamp:
                largest_value = value
                largest_timestamp = timestamp_prev

        return largest_value

