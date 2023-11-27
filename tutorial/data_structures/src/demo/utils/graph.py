from collections import defaultdict
from demo.utils import Node

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, a: Node, b:Node) -> None:
        self.graph[a].append(b)
        self.graph[b].append(a)

    def hasEdge(self, a: Node, b: Node) -> bool:
        return b in self.graph[a]
    
    def getAdjList(self, a: Node) -> list[Node]:
        if a in self.graph:
            return  self.graph[a]
        else:
            return None


    
class DirectedGraph(Graph):
    def __init__(self):
        super(DirectedGraph, self).__init__()

    def addEdge(self, a: Node, b: Node) -> None:
        self.graph[a].append(b)

    
    


    

