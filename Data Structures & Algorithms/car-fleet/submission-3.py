class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for ind in range(len(position)):
            cars.append((position[ind], speed[ind]))
        cars.sort()

        fleets = []

        for ind in range(len(cars) - 1, -1, -1):
            if not fleets:
                fleets.append(cars[ind])
                continue
            
            nextCar = fleets[-1]
            first = (target - cars[ind][0]) / cars[ind][1]
            second = (target - nextCar[0]) / nextCar[1]

            if first > second:
                fleets.append(cars[ind])
                

        return len(fleets)