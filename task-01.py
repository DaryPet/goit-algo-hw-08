import heapq

def minimum_cost_to_connect_cables(cables):
    # convert list to heap
    heapq.heapify(cables)
    # total cost for connections for all cables
    total_cost = 0

    # while we have more than 1 cable we will conect 2 shortest
    while len(cables) > 1:
        # take 2 shortest
        cable1 = heapq.heappop(cables)
        cable2 = heapq.heappop(cables)
        # cost for 2 cables
        combined_cables = cable1 + cable2
        total_cost += combined_cables
    return total_cost

# example of use
cables =[4,3,7.6]
min_cost = minimum_cost_to_connect_cables(cables)
print("Minimum cost of connected cables is:", min_cost)
