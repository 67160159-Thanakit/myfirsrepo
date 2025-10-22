class Graph:
    def __init__(self):
        self.graph = {}  # เก็บโครงสร้างกราฟในรูปแบบ dictionary

    def add_edge(self, u, v):
        """เพิ่มเส้นเชื่อม (edge) ระหว่างจุดยอด u และ v"""
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs(self, start):
        """Breadth-First Search"""
        visited = set()
        queue = [start]

        print("BFS Traversal:", end=" ")
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                # เพิ่มเพื่อนบ้านของ vertex ที่ยังไม่ถูกเยี่ยมเข้า queue
                queue.extend([n for n in self.graph.get(vertex, []) if n not in visited])
        print()

    def dfs(self, start, visited=None):
        """Depth-First Search (ใช้ recursion)"""
        if visited is None:
            visited = set()

        print(start, end=" ")
        visited.add(start)

        for neighbor in self.graph.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

# 🔹 ตัวอย่างการใช้งาน
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'E')
g.add_edge('D', 'F')
g.add_edge('E', 'F')

print("โครงสร้างกราฟ:", g.graph)

print("\nผลลัพธ์จาก BFS และ DFS:")
g.bfs('A')
print("DFS Traversal:", end=" ")
g.dfs('A')
print()
