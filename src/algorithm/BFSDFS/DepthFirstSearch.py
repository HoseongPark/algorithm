"""
그래프 구현은 = Dict + List 로 구현
visitedQueue, needVisitStack = List로 구현
"""

def dfs(graph, startNode):
    visitedQueue = list()
    needVisitStack = list()

    needVisitStack.append(startNode)

    while needVisitStack:
        popData = needVisitStack.pop()

        if popData not in visitedQueue:
            visitedQueue.append(popData)
            needVisitStack.extend(graph[popData])
            
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

    print(dfs(graph, "A"))