class CountSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        if not point[0] in self.points:
            self.points[point[0]] = defaultdict(int)
        self.points[point[0]][point[1]] += 1
        print(self.points)

    def count(self, point: List[int]) -> int:
        if not point[0] in self.points:
            return 0
            
        count = 0
        for col in self.points[point[0]]:
            if point[1] == col:
                continue
            size = abs(col - point[1])
            if point[0] - size in self.points and point[1] in self.points[point[0] - size] and col in self.points[point[0] - size]:
                count += self.points[point[0]][col] * self.points[point[0] - size][point[1]] * self.points[point[0] - size][col]
            if point[0] + size in self.points and point[1] in self.points[point[0] + size] and col in self.points[point[0] + size]:
                count += self.points[point[0]][col] * self.points[point[0] + size][point[1]] * self.points[point[0] + size][col]

        return count