class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ticketMap = defaultdict(list)
        flights = defaultdict(int)

        tickets.sort(key=lambda x: (x[0], x[1]))

        for ticket in tickets:
            ticketMap[ticket[0]].append(ticket[1])
            flights[(ticket[0], ticket[1])] += 1

        result = ["JFK"]
        def traverse(airport):
            if len(result) == len(tickets) + 1:
                return True
            if len(ticketMap[airport]) == 0:
                return False

            temp = ticketMap[airport]
            for index, neighbor in enumerate(temp):
                ticketMap[airport].pop(index)
                result.append(neighbor)
                visit = traverse(neighbor)
                if visit:
                    return True
                result.pop()
                ticketMap[airport].insert(index, neighbor)

            return False

        traverse("JFK")
        return result