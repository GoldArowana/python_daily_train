"""
@arthor:金龙
@school:哈尔滨理工大学
@department:计算机学院
@time: 2017/9/24 22:01
@describe:在这里实现了图的理解矩阵的相关操作，
    并实现了图的深度搜索(dfs)和图的广度搜索(bfs)
"""


class Graph:
    """这个类是：一个图数据结构"""

    def __init__(self, var_map):
        # 1.接收传来的邻接矩阵值
        self.graph_map = var_map
        # 2.将邻接矩阵转化为无向图的形式
        self.toNoDirect()
        # 3.属性：结点数
        self.node_number = self.getNodeNumber()
        # 4.属性：边数
        self.edge_number = self.getEdgeNumber()
        # 5.属性：bfs结果
        self.router_bfs = []
        # 6.属性：dfs结果
        self.router_dfs = []

    def toNoDirect(self):
        """"这个方法的功能是：将有向图变为无向图"""
        for row in range(len(self.graph_map)):
            for col in range(row):
                summery = self.graph_map[row][col] + self.graph_map[col][row]
                # 构造对称矩阵
                # 构造原则：(x,y)和(y,x)当中，只要其中一个为 1, 则让它俩都为 1
                if summery > 0:
                    self.graph_map[row][col] = 1
                    self.graph_map[col][row] = 1

    def getNodeNumber(self):
        """"这个方法的功能是：取得图中结点的个数"""
        return len(self.graph_map)

    def getEdgeNumber(self):
        """这个方法的功能是：取得图中边的个数"""
        self.edge_number = 0
        for row in range(self.node_number):
            for col in range(self.node_number):
                if self.graph_map[row][col] is 1:
                    self.edge_number = self.edge_number + 1
        return self.edge_number // 2

    def addNode(self):
        """这个方法的功能是：向图中添加一个结点"""
        for i in range(self.node_number):
            # 利用for循环在map里添加一列 0
            self.graph_map[i].append(0)
        self.node_number = self.node_number + 1
        # 用*来构造一行 0
        oneRow = [0] * self.node_number
        # 在map里添加一行0
        self.graph_map.append(oneRow)
        # 让对角线上的元素为 -1
        self.graph_map[self.node_number - 1][self.node_number - 1] = -1

    def addEdge(self, x, y):
        """这个方法的功能是：向图中添加结点"""
        if self.graph_map[x][y] is 0:
            self.graph_map[x][y] = 1
            self.graph_map[y][x] = 1
            self.edge_number = self.edge_number + 1

    def removeEdge(self, x, y):
        """这个方法的功能是：在图中删除结点(x,y)"""
        if self.graph_map[x][y] is 1:
            self.graph_map[x][y] = 0
            self.graph_map[y][x] = 0
            self.edgenum = self.edgenum - 1

    def callBFS(self):
        """实现BFS功能"""

        def BFS(self, i):
            """BFS递归体"""
            self.router_bfs.append(i)
            visited[i] = 1
            for k in range(self.node_number):
                if self.graph_map[i][k] == 1 and visited[k] == 0:
                    BFS(self, k)

        # 遍历结点
        visited = [0] * self.node_number
        for i in range(self.node_number):
            if visited[i] is 0:
                BFS(self, i)

    def callDFS(self):
        """实现DFS功能"""

        def DFS(self, i, queue):
            """DFS迭代体"""
            queue.append(i)
            self.router_dfs.append(i)
            visited[i] = 1
            if len(queue) != 0:
                w = queue.pop()
                for k in range(self.node_number):
                    if self.graph_map[w][k] is 1 and visited[k] is 0:
                        DFS(self, k, queue)

        # 遍历结点
        visited = [0] * self.node_number
        queue = []
        for i in range(self.node_number):
            if visited[i] is 0:
                DFS(self, i, queue)

    def printNodeNumber(self):
        """这个方法的功能是：个性化地打印图中结点个数"""
        print("该图的结点个数是：", self.node_number)

    def printEdgeNumber(self):
        """这个方法的功能是：个性化地打印图中边的个数"""
        print("该图的边的个数是：", self.edge_number)

    def printMap(self):
        """这个方法的功能是：个性化地打印邻接矩阵"""
        print("---------------------------MAP START------------------------\n")
        for row in range(self.node_number):
            for col in range(self.node_number):
                print("%6d" % self.graph_map[row][col], end='')
            print()
        print("\n---------------------------MAP END--------------------------")

    def printBFS(self):
        """这个方法的功能是：个性化地打印BFS的结果"""
        for i in range(len(self.router_bfs)):
            print(self.router_bfs[i], end=" -> ")
        print("完成")

    def printDFS(self):
        """这个方法的功能是：个性化地打印DFS的结果"""
        for i in range(len(self.router_dfs)):
            print(self.router_dfs[i], end=" -> ")
        print("完成")


def myTest():
    """
    此方法是测试方法。
    主要用来测试功能
    并输出结果
    """
    graph_map = [
        [-1, 1, 0, 0],
        [0, -1, 0, 0],
        [0, 0, -1, 1],
        [1, 0, 0, -1]
    ]
    graph = Graph(graph_map)
    graph.addNode()
    graph.addEdge(1, 4)
    graph.addEdge(1, 3)
    graph.printMap()
    graph.printNodeNumber()
    graph.printEdgeNumber()
    graph.callBFS()
    graph.printBFS()
    graph.callDFS()
    graph.printDFS()


if __name__ == '__main__':
    """此方法是主方法。此处为整个函数的入口"""
    myTest()
