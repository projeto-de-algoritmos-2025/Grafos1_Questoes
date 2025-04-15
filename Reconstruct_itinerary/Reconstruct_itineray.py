from collections import defaultdict
import heapq

class Solution:
    def findItinerary(self, tickets):
        graph = defaultdict(list)
        
        for src, dst in tickets:
            heapq.heappush(graph[src], dst)

        result = []

        def visit(airport):
            while graph[airport]:
                next_dest = heapq.heappop(graph[airport])
                visit(next_dest)
            result.append(airport)

        visit("JFK")
        return result[::-1]
