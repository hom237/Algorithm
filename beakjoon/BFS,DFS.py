okNode = [[], []]
edgeList = []

def DFS(edgelist, nownode):
    global okNode, edgeList
    okNode[0].append(nownode)
    try:
        for i in range(len(edgelist)):
            if nownode in edgelist[i]:
                if edgelist[i][0] == nownode:
                    targetNode = edgelist[i][1]
                else:
                    targetNode = edgelist[i][0]
                if not(targetNode in okNode[0]):
                    DFS(edgelist, targetNode)
        return nownode
    except:
        return nownode
def BFS(edgelist, nownode, bfsEdgeList):
    global okNode
    bfsEdgeList.pop(0)
    okNode[1].append(nownode)
    try:
        for i in range(len(edgelist)):
            if nownode in edgelist[i]:
                if edgelist[i][0] == nownode:
                    targetNode = edgelist[i][1]
                else:
                    targetNode = edgelist[i][0]
                if not(targetNode in bfsEdgeList) and not(targetNode in okNode[1]):
                    bfsEdgeList.append(targetNode)
        BFS(edgelist, bfsEdgeList[0], bfsEdgeList)
    except:
        return nownode


nodeNum, edgeNum, startNode = map(int, input().split())
for i in range(edgeNum):
    edgeList.append(sorted(list(map(int, input().split()))))
edgeList = sorted(edgeList)
bfsEdgeList = [startNode]
DFS(edgeList, startNode)
BFS(edgeList, startNode, bfsEdgeList)
print(*okNode[0])
print(*okNode[1])