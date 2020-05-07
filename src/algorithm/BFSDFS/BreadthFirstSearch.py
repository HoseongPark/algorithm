"""
그래프 구현은 = Dict + List 로 구현
visitedQueue, needVisitQueue = List로 구현
"""

def bfs(graph, startNode):
    visitedQueue = list()
    needVisitQueue = list()

    needVisitQueue.append(startNode)

    while needVisitQueue:
        popData = needVisitQueue.pop(0)

        if popData not in visitedQueue:
            visitedQueue.append(popData)
            needVisitQueue.extend(graph[popData])
            
    return visitedQueue


if __name__ == "__main__":

    graph = dict()
    graph["A"] = ["B", "C"]
    graph["B"] = ["A", "D"]
    graph["C"] = ["A", "E", "F"]
    graph["D"] = ["B", "G"]
    graph["E"] = ["C"]
    graph["F"] = ["C", "H"]
    graph["G"] = ["D"]
    graph["H"] = ["F"]

    print(bfs(graph, "A"))