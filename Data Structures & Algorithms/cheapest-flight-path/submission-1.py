class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        count = 0

        current = {} 
        for airport in range(0, n):
            current[airport] = float("inf")
        current[src] = 0

        while count < k + 1:
            new = {}
            for fromI, toI, priceI in flights:
                if current[fromI] == float("inf"):
                    continue
                fromPrice = current[fromI]

                if toI in new:
                    new[toI] = min(new[toI], fromPrice + priceI)
                else:
                    new[toI] = fromPrice + priceI
                
            for stop in new:
                if new[stop] < current[stop]:
                    current[stop] = new[stop]
            count += 1

        if current[dst] == float("inf"):
            return -1
        return current[dst]