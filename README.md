# Practical 8: Graph Traversal Algorithms (Depth-First Search & Breadth-First Search)

This directory contains the Python implementation of core graph traversal algorithms: **Depth-First Search (DFS)** and **Breadth-First Search (BFS)** on undirected graphs represented via an **Adjacency List**. The program measures and compares execution runtimes using `time.perf_counter()`.

---

## 📌 Problem Overview & Concepts

Graph traversal refers to the process of visiting all the vertices (nodes) in a graph systematic search pattern.

### Graph Representation
The graph is represented using an **Adjacency List** using Python's `collections.defaultdict(list)` for efficient $\mathcal{O}(1)$ neighbor lookup and $\mathcal{O}(V + E)$ space complexity.

### Algorithms Implemented

1. **Depth-First Search (DFS) (`dfs(start)`)**
   - Traverses deeply along each branch of the graph before backtracking.
   - Uses recursion (implicit call stack) to keep track of visited nodes.
   - **Time Complexity:** $\mathcal{O}(V + E)$ where $V$ is the number of vertices and $E$ is the number of edges.
   - **Space Complexity:** $\mathcal{O}(V)$ due to the boolean `visited` array and recursion call stack frame.
   - **Applications:** Topological sorting, detecting cycles, connected components, solving mazes/puzzles.

2. **Breadth-First Search (BFS) (`bfs(start)`)**
   - Explores nodes level-by-level, visiting all immediate neighbors of a vertex before proceeding to the next level.
   - Uses an explicit First-In-First-Out (FIFO) queue (`collections.deque`) to manage node exploration.
   - **Time Complexity:** $\mathcal{O}(V + E)$
   - **Space Complexity:** $\mathcal{O}(V)$ for storing nodes in the queue and visited array.
   - **Applications:** Shortest path in unweighted graphs, web crawlers, social network connection levels (degrees of separation), minimum spanning tree (Bipartite testing).

---

## ⚡ Complexity Summary

| Algorithm | Time Complexity | Auxiliary Space | Underlying Data Structure | Exploration Strategy |
| :--- | :---: | :---: | :---: | :--- |
| **Depth-First Search (DFS)** | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ | Recursion Stack | Deep-first / Branch-by-branch |
| **Breadth-First Search (BFS)** | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ | FIFO Queue (`deque`) | Level-by-level / Radial |

---

## 💻 How to Run

1. Open your terminal or command prompt.
2. Navigate to the `practical_8` directory:
   ```bash
   cd practical_8
   ```
3. Execute the Python script:
   ```bash
   python graph_traversal.py
   ```

---

## 📋 Sample Input & Output

### Input Example (Graph with 5 Vertices and 6 Edges):
```text
Enter number of vertices: 5
Enter number of edges: 6
Enter edges (u v):
0 1
0 2
1 3
1 4
2 4
3 4
Enter starting vertex: 0
```

### Execution Output:
```text
DFS Traversal: 0 1 3 4 2
BFS Traversal: 0 1 2 3 4

Execution Time:
DFS: 5399.98 ns
BFS: 7900.00 ns

=======================================================
         GRAPH TRAVERSAL COMPLEXITY SUMMARY
=======================================================
Method     | Time Complexity    | Space Complexity  
-------------------------------------------------------
DFS        | O(V + E)           | O(V)              
BFS        | O(V + E)           | O(V)              
=======================================================
```

---

## 📖 Key Takeaways & Conclusion

1. **Traversal Paradigms**:
   - **DFS** dives deep into a single branch until dead-end before backtracking, making it ideal for path-finding, topological ordering, and constraint satisfaction.
   - **BFS** expands uniformly outwards level-by-level, guaranteeing the shortest path in unweighted graphs.
2. **Efficiency**:
   - Both DFS and BFS achieve linear time complexity $\mathcal{O}(V + E)$ relative to graph size, making them optimal search methods for arbitrary graph topologies.
