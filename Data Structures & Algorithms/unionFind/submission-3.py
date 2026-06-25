class UnionFind:
    
    def __init__(self, n: int):
        self.rank = {}
        self.parent = {}
        self.component_count = n

        for i in range(n):
            self.rank[i] = 0
            self.parent[i] = i

    def find(self, x: int) -> int:
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        if self.isSameComponent(x, y):
            return False
        
        root_x, root_y = self.find(x), self.find(y)
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        elif self.rank[root_y] > self.rank[root_x]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        self.component_count -= 1
        return True

    def getNumComponents(self) -> int:
        return self.component_count

"""
0 - 1
  - 2 - 3
"""