class Graph:
    # 无向图, 邻接表
    def __init__(self, family=None):
        self.node_neighbors = {}

    @property
    def nodes(self):
        # 所有顶点
        return self.node_neighbors.keys()

    def neighbors(self, u):
        # 顶点u的所有邻接点
        return self.node_neighbors.get(u, set())

    def add_node(self, node):
        # 添加一个顶点
        if  node not in self.nodes:
            self.node_neighbors[node] = set()

    def add_nodes(self, nodelist):
        # 添加多个顶点
        for node in nodelist:
            self.add_node(node)

    def add_edge(self, edge):
        # 添加一条边
        u, v = edge
        if u not in self.nodes or v not in self.nodes:
            print('error has no node %s or %s .' % (str(u), str(v)))
        self.node_neighbors.get(u).add(v)
        self.node_neighbors.get(v).add(u)

    def add_edges(self, edges):
        # 添加多条边
        for u, v in edges:
            self.add_edge((u, v))

    def depth_first_search(self, root=None):
        # 深度优先遍历
        # 用stack存储遍历过的顶点，先进后出

        stack = []
        visited = set()

        def dfs():
            while stack:
                node = stack.pop()
                visited.add(node)
                print(node,)
                for n in self.neighbors(node):
                    if n not in visited:
                        stack.append(n)
                        visited.add(node)
            print('--',)

        if root:
            stack.append(root)
            dfs()

        for node in self.nodes:
            if node not in visited:
                stack.append(node)
                dfs()
        print()

    def breadth_first_search(self, root=None):
        # 广度优先遍历
        # 用queue存储遍历的过的顶点， 先进先出

        queue = []
        visited = set()

        def bfs():
            while queue:
                node = queue.pop(0)
                visited.add(node)
                print(node,)
                for n in self.neighbors(node):
                    if n not in visited:
                        queue.append(n)
                        visited.add(node)
            print('--')

        if root:
            queue.append(root)
            bfs()

        for node in self.nodes:
            if node not in visited:
                queue.append(node)
                bfs()
        print()

    def test(self):
        self.add_nodes([i for i in range(1, 9)])
        print("nodes:", self.nodes)

        self.add_edge((1, 2))
        self.add_edge((1, 3))
        self.add_edge((2, 3))
        self.add_edge((6, 2))
        self.add_edge((4, 5))
        self.add_edge((6, 7))
        self.add_edge((3, 5))

        print('广度遍历:')
        self.breadth_first_search(1)
        print('深度遍历:')
        self.depth_first_search(1)


p = Graph()
p.test()
