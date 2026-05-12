class TimeMap:

    def __init__(self):
        self.values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.values[key]
        if len(values) == 0:
            return ""

        left = 0
        right = len(values) - 1
        while left < right:
            mid = (left + right) // 2
            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid

        result = ""
        if values[left][0] <= timestamp:
            result = values[left][1]
        elif left > 0:
            result = values[left - 1][1]
        return result
