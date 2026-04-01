class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for index in range(len(intervals)):
            if newInterval[1] < intervals[index][0]:
                res.append(newInterval)
                return res + intervals[index:]
            elif newInterval[0] > intervals[index][1]:
                res.append(intervals[index])
            else:
                newInterval = [min(newInterval[0], intervals[index][0]), max(newInterval[1], intervals[index][1])]
        
        res.append(newInterval)
        return res