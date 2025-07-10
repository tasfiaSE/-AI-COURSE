
## 1️⃣ Alpha-Beta Pruning

### 📌 How it works
Alpha-Beta Pruning is an optimization of the Minimax algorithm. It prunes branches that cannot affect the final decision, reducing the search space.

### 🎯 Applications
- 2-player adversarial games (e.g., Chess, Checkers)
- AI decision making in games

### ⏱️ Complexity
- Time: O(b^d), improved to O(b^(d/2)) with good pruning
- Space: O(d)

## 2️⃣ AO* Algorithm

### 📌 How it works
AO* is a best-first search algorithm for solving problems represented by AND-OR graphs. It chooses the most promising path based on cost and expands it.

### 🎯 Applications
- Problem-solving in expert systems
- Knowledge representation with AND-OR graphs

### ⏱️ Complexity
- Time: Exponential in worst case
- Space: O(n)

---

## 3️⃣ Beam Search

### 📌 How it works
Beam Search is a heuristic version of BFS. It explores a limited number of best nodes at each level to control memory and time usage.

### 🎯 Applications
- Speech recognition
- Machine translation
- Natural Language Processing

### ⏱️ Complexity
- Time: O(b^k) where k = beam width
- Space: O(bk)

---

## 4️⃣ Breadth-First Search (BFS)

### 📌 How it works
BFS explores all neighbor nodes level by level. It uses a queue to keep track of nodes to visit.

### 🎯 Applications
- Shortest path in unweighted graphs
- Web crawlers
- Peer-to-peer networks

### ⏱️ Complexity
- Time: O(V + E)
- Space: O(V)


---

## 5️⃣ Bidirectional Search

### 📌 How it works
Bidirectional Search runs two simultaneous searches — one forward from the start node and one backward from the goal — and stops when they meet.

### 🎯 Applications
- Faster shortest path finding
- Road maps & navigation systems

### ⏱️ Complexity
- Time: O(b^(d/2))
- Space: O(b^(d/2))

---

## 6️⃣ Depth-First Search (DFS)

### 📌 How it works
DFS explores as far as possible along each branch before backtracking. It uses a stack (can be implicit via recursion).

### 🎯 Applications
- Path finding in mazes
- Topological sorting
- Solving puzzles

### ⏱️ Complexity
- Time: O(V + E)
- Space: O(V)

---

## 7️⃣ Hill Climbing

### 📌 How it works
Hill Climbing is a heuristic search that moves towards the neighbor with the highest value. It stops when it reaches a peak.

### 🎯 Applications
- Local search optimization
- Robotics path planning
- Machine learning tuning

### ⏱️ Complexity
- Time: Depends on step size & problem space
- Space: O(1)

---

## 8️⃣ Min-Max Algorithm

### 📌 How it works
Min-Max is a backtracking algorithm for decision making in adversarial games. It assumes both players play optimally to maximize or minimize the score.

### 🎯 Applications
- Chess, Tic-Tac-Toe AI
- Any 2-player zero-sum game

### ⏱️ Complexity
- Time: O(b^d)
- Space: O(bd)


---

