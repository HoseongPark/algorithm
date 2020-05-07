import heapq

def dijkstra(graph, startNode):
    distance = {node: float('inf') for node in graph}
    distance[startNode] = 0

    minHeap = []
    heapq.heappush(minHeap, [distance[startNode], startNode])

    while minHeap:
        minWeight, minKey = heapq.heappop(minHeap)

        if distance[minKey] < minWeight:
            continue

        for key, weight in graph[minKey].items():
            if minWeight + weight < distance[key]:
                distance[key] = minWeight + weight
                heapq.heappush(minHeap, [weight, key])

    print(distance)

if __name__ == "__main__":
    
    graph = {
        '1': {'2': 10, '3': 50, '4': 30, '5': 200},
        '2': {'3': 40},
        '3': {'5': 10},
        '4': {'3': 60, '5': 20},
        '5': {}
    }

    dijkstra(graph, '1')