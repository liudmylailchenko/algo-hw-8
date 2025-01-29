import heapq


def min_cost_to_connect_cables(cables):
    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        cost = first + second
        total_cost += cost
        heapq.heappush(cables, cost)

    return total_cost


cables = [5, 4, 10, 7, 3, 8, 6, 2]

print(min_cost_to_connect_cables(cables))
