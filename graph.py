class Graph():
    def __init__(self):
        self.graph_lyst = [[-1] * 10 for i in range(10)]
        self.label_lyst = []


    def add_vertex(self, label):
        self.label_lyst.append(str(label))
        return self.graph_lyst


    def add_edge(self, src, dest, w):
        self.graph_lyst[src[self.graph_lyst.index()]][dest] = w
        return self.graph_lyst


    def get_weight(self, src, dest):
        return


    def dfs(self, starting_vertex):
        return


    def bfs(self, starting_vertex):
        return


    def dijkstra_shortest_path(self, src):
        return


    def __str__(self):
        return

def main():
    Graph.add_edge(1,2,5)

main()

