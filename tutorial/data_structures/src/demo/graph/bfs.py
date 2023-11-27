from demo.utils.graph import Graph
from demo.utils.node import Node

def bfs(g: Graph, source: Node) -> list[Node]:
    queue = []
    visited = set()
    res = []
    queue.append(source)

    while queue:
        node = queue.pop(0)
        visited.add(node)
        res.append(node.val)
        
        for n in g.getAdjList(node):
            if n not in visited:
                queue.append(n)

    return res


if __name__ == '__main__':

    g = Graph()

    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print(bfs(g, 2))
