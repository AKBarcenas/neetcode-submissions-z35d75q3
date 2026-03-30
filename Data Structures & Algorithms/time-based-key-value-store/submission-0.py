class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.map:
            return ""

        values = self.map[key]

        left = 0
        right = len(values) - 1
        result = ""
        while left <= right:
            mid = (left + right) // 2
            curr = values[mid]
            if curr[0] > timestamp:
                right = mid - 1
            else:
                left = mid + 1
                result = curr[1]

        return result