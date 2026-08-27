import collections
import time


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.adj = collections.defaultdict(list)

    def add_edge(self, u, v):
        """Adds an undirected edge between vertex u and vertex v."""
        self.adj[u].append(v)
        self.adj[v].append(u)

    def dfs(self, start):
        """
        Depth-First Search (DFS) implementation using recursion.
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        """
        visited = [False] * self.V
        order = []

        def dfs_util(v):
            visited[v] = True
            order.append(v)
            for neighbor in self.adj[v]:
                if not visited[neighbor]:
                    dfs_util(neighbor)

        dfs_util(start)
        return order

    def bfs(self, start):
        """
        Breadth-First Search (BFS) implementation using a Queue.
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        """
        visited = [False] * self.V
        order = []
        queue = collections.deque([start])
        visited[start] = True

        while queue:
            node = queue.popleft()
            order.append(node)

            for neighbor in self.adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return order


def main():
    try:
        V = int(input("Enter number of vertices: "))
        g = Graph(V)

        E = int(input("Enter number of edges: "))
        print("Enter edges (u v):")
        for _ in range(E):
            u, v = map(int, input().split())
            g.add_edge(u, v)

        start = int(input("Enter starting vertex: "))
    except (ValueError, IndexError):
        print("Invalid input! Please enter valid integers for graph definition.")
        return

    # DFS Time Analysis
    start_dfs = time.perf_counter()
    dfs_order = g.dfs(start)
    end_dfs = time.perf_counter()
    dfs_time_ns = (end_dfs - start_dfs) * 1e9

    # BFS Time Analysis
    start_bfs = time.perf_counter()
    bfs_order = g.bfs(start)
    end_bfs = time.perf_counter()
    bfs_time_ns = (end_bfs - start_bfs) * 1e9

    # Print Results
    print("\nDFS Traversal: " + " ".join(map(str, dfs_order)))
    print("BFS Traversal: " + " ".join(map(str, bfs_order)))

    print("\nExecution Time:")
    print(f"DFS: {dfs_time_ns:.2f} ns")
    print(f"BFS: {bfs_time_ns:.2f} ns")

    # Complexity Summary
    print("\n" + "=" * 55)
    print("         GRAPH TRAVERSAL COMPLEXITY SUMMARY")
    print("=" * 55)
    print(f"{'Method':<10} | {'Time Complexity':<18} | {'Space Complexity':<18}")
    print("-" * 55)
    print(f"{'DFS':<10} | {'O(V + E)':<18} | {'O(V)':<18}")
    print(f"{'BFS':<10} | {'O(V + E)':<18} | {'O(V)':<18}")
    print("=" * 55)


if __name__ == "__main__":
    main()
