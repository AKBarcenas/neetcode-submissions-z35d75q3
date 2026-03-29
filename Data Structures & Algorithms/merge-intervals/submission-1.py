class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 1:
            return []
        if len(intervals) == 1:
            return intervals
        intervals.sort(key=lambda i: i[0])

        results = []
        current = intervals[0]
        for index in range(1,len(intervals)):
            if current[1] >= intervals[index][0]:
                if current[1] < intervals[index][1]:
                    current[1] = intervals[index][1]
            else:
                results.append(current)
                current = intervals[index]

        results.append(current)
        return results