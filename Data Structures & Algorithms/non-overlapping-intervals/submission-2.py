class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort(key=lambda x: x[0])
        currentEnd = intervals[0][1]

        for index in range(1, len(intervals)):
            if intervals[index][0] < currentEnd:
                count += 1
                currentEnd = min(currentEnd, intervals[index][1]) 
            else:
                currentEnd = intervals[index][1]
        return count