# Checklist de Tópicos - Google Interview

## 📋 Progreso General

- [ ] Completar plan de 12 días
- [ ] Resolver 100+ problemas
- [ ] Realizar al menos 1 mock interview
- [ ] Completar todas las implementaciones clave

---

## 1️⃣ Algorithm Complexity (Big O)

### Teoría
- [ ] Big O notation (tiempo)
- [ ] Big O notation (espacio)
- [ ] Mejor, promedio, peor caso
- [ ] Análisis amortizado
- [ ] Common complexities: O(1), O(log n), O(n), O(n log n), O(n²), O(2^n)

### Práctica
- [ ] Analizar complejidad de 20+ algoritmos
- [ ] Identificar bottlenecks en código
- [ ] Optimizar soluciones de O(n²) a O(n)

### Recursos
- [ ] Cracking Interview Cap. VI
- [ ] [Big O Cheat Sheet](https://www.bigocheatsheet.com/)

---

## 2️⃣ Arrays y Strings

### Conceptos
- [ ] Array traversal (forward, backward)
- [ ] Two pointers technique
- [ ] Sliding window
- [ ] String manipulation
- [ ] Palindromes
- [ ] Anagrams

### Problemas (15-20)
- [ ] Two Sum
- [ ] Best Time to Buy and Sell Stock
- [ ] Contains Duplicate
- [ ] Valid Anagram
- [ ] Group Anagrams
- [ ] Top K Frequent Elements
- [ ] Product of Array Except Self
- [ ] Encode and Decode Strings
- [ ] Longest Consecutive Sequence
- [ ] Valid Palindrome
- [ ] Longest Substring Without Repeating Characters
- [ ] Longest Repeating Character Replacement
- [ ] Minimum Window Substring

### Implementaciones
- [ ] `practice/data_structures/arrays.py`
- [ ] `practice/data_structures/strings.py`
- [ ] Two pointers examples
- [ ] Sliding window examples

---

## 3️⃣ Sorting & Searching

### Teoría
- [ ] QuickSort - O(n log n)
- [ ] MergeSort - O(n log n)
- [ ] HeapSort - O(n log n)
- [ ] Binary Search - O(log n)
- [ ] Binary Search variantes
- [ ] Stability en sorting

### Problemas (10-12)
- [ ] Binary Search
- [ ] Search in Rotated Sorted Array
- [ ] Find Minimum in Rotated Sorted Array
- [ ] Search a 2D Matrix
- [ ] Koko Eating Bananas
- [ ] Find First and Last Position of Element
- [ ] Time Based Key-Value Store

### Implementaciones
- [ ] `practice/algorithms/sorting.py` (QuickSort, MergeSort)
- [ ] `practice/algorithms/binary_search.py`
- [ ] Binary search on answer pattern

---

## 4️⃣ Hash Tables

### Teoría
- [ ] Hash function design
- [ ] Collision resolution (chaining, open addressing)
- [ ] Load factor
- [ ] Time complexity: O(1) average
- [ ] Python dict internals

### Problemas (8-10)
- [ ] Two Sum (revisión)
- [ ] Group Anagrams (revisión)
- [ ] Valid Sudoku
- [ ] Longest Substring Without Repeating Characters
- [ ] Minimum Window Substring
- [ ] LRU Cache

### Implementaciones
- [ ] `practice/data_structures/hash_table.py`
- [ ] Implementar hash function simple
- [ ] Resolver colisiones con chaining

---

## 5️⃣ Linked Lists

### Conceptos
- [ ] Singly Linked List
- [ ] Doubly Linked List
- [ ] Circular Linked List
- [ ] Fast & Slow pointers
- [ ] Reverse linked list

### Problemas (8-10)
- [ ] Reverse Linked List
- [ ] Merge Two Sorted Lists
- [ ] Linked List Cycle
- [ ] Remove Nth Node From End
- [ ] Reorder List
- [ ] Merge K Sorted Lists

### Implementaciones
- [ ] `practice/data_structures/linked_list.py`
- [ ] Reverse iterativo y recursivo
- [ ] Floyd's cycle detection

---

## 6️⃣ Stacks & Queues

### Conceptos
- [ ] Stack (LIFO)
- [ ] Queue (FIFO)
- [ ] Monotonic stack
- [ ] Deque
- [ ] Priority Queue (heap)

### Problemas (6-8)
- [ ] Valid Parentheses
- [ ] Min Stack
- [ ] Evaluate Reverse Polish Notation
- [ ] Daily Temperatures
- [ ] Car Fleet
- [ ] Largest Rectangle in Histogram

### Implementaciones
- [ ] `practice/data_structures/stack.py`
- [ ] `practice/data_structures/queue.py`
- [ ] Stack usando arrays
- [ ] Queue usando linked list

---

## 7️⃣ Trees

### Teoría
- [ ] Binary Tree basics
- [ ] Binary Search Tree (BST)
- [ ] Balanced trees (AVL concept)
- [ ] Traversals: Inorder, Preorder, Postorder
- [ ] Level-order traversal (BFS)
- [ ] DFS en trees
- [ ] Lowest Common Ancestor

### Problemas (20-25)

#### Easy
- [ ] Invert Binary Tree
- [ ] Maximum Depth of Binary Tree
- [ ] Same Tree
- [ ] Subtree of Another Tree
- [ ] Lowest Common Ancestor of BST
- [ ] Balanced Binary Tree

#### Medium
- [ ] Binary Tree Level Order Traversal
- [ ] Binary Tree Right Side View
- [ ] Count Good Nodes in Binary Tree
- [ ] Validate Binary Search Tree
- [ ] Kth Smallest Element in BST
- [ ] Construct Binary Tree from Preorder and Inorder
- [ ] Diameter of Binary Tree
- [ ] Serialize and Deserialize Binary Tree
- [ ] Binary Tree Maximum Path Sum

### Implementaciones
- [ ] `practice/data_structures/binary_tree.py`
- [ ] `practice/data_structures/bst.py`
- [ ] `practice/algorithms/tree_traversals.py`
- [ ] Inorder (iterativo y recursivo)
- [ ] Preorder (iterativo y recursivo)
- [ ] Postorder (iterativo y recursivo)
- [ ] Level-order (BFS)

---

## 8️⃣ Graphs

### Teoría
- [ ] Graph representations (adjacency list, matrix, edge list)
- [ ] BFS (Breadth-First Search)
- [ ] DFS (Depth-First Search)
- [ ] Topological Sort
- [ ] Dijkstra's algorithm (opcional)
- [ ] Union-Find (Disjoint Set)
- [ ] Cycle detection

### Problemas (15-20)

#### Medium
- [ ] Number of Islands
- [ ] Clone Graph
- [ ] Max Area of Island
- [ ] Pacific Atlantic Water Flow
- [ ] Surrounded Regions
- [ ] Rotting Oranges
- [ ] Walls and Gates
- [ ] Course Schedule
- [ ] Course Schedule II
- [ ] Graph Valid Tree
- [ ] Number of Connected Components in Undirected Graph
- [ ] Redundant Connection

#### Hard (opcional)
- [ ] Word Ladder
- [ ] Alien Dictionary

### Implementaciones
- [ ] `practice/data_structures/graph.py`
- [ ] `practice/algorithms/bfs.py`
- [ ] `practice/algorithms/dfs.py`
- [ ] BFS iterativo (queue)
- [ ] DFS recursivo
- [ ] DFS iterativo (stack)
- [ ] Topological sort
- [ ] Union-Find

---

## 9️⃣ Heaps / Priority Queue

### Teoría
- [ ] Min Heap
- [ ] Max Heap
- [ ] Heapify operation
- [ ] Time complexity: insert O(log n), extract O(log n)
- [ ] Python heapq module

### Problemas (6-8)
- [ ] Kth Largest Element in Array
- [ ] K Closest Points to Origin
- [ ] Task Scheduler
- [ ] Find Median from Data Stream
- [ ] Merge K Sorted Lists

### Implementaciones
- [ ] `practice/data_structures/heap.py`
- [ ] Min Heap implementation
- [ ] Heapify

---

## 🔟 Recursion

### Conceptos
- [ ] Base case
- [ ] Recursive case
- [ ] Call stack
- [ ] Tail recursion
- [ ] Backtracking

### Problemas (8-10)
- [ ] Subsets
- [ ] Combination Sum
- [ ] Permutations
- [ ] Letter Combinations of Phone Number
- [ ] Palindrome Partitioning
- [ ] Word Search
- [ ] N-Queens (opcional)

### Implementaciones
- [ ] `practice/algorithms/recursion.py`
- [ ] Factorial
- [ ] Fibonacci (recursivo)
- [ ] Backtracking template

---

## 1️⃣1️⃣ Dynamic Programming

### Conceptos
- [ ] Memoization (top-down)
- [ ] Tabulation (bottom-up)
- [ ] Overlapping subproblems
- [ ] Optimal substructure
- [ ] 1-D DP
- [ ] 2-D DP

### Problemas (12-15)

#### 1-D DP
- [ ] Climbing Stairs
- [ ] House Robber
- [ ] House Robber II
- [ ] Longest Palindromic Substring
- [ ] Palindromic Substrings
- [ ] Decode Ways
- [ ] Coin Change
- [ ] Maximum Product Subarray
- [ ] Word Break
- [ ] Longest Increasing Subsequence

#### 2-D DP
- [ ] Unique Paths
- [ ] Longest Common Subsequence
- [ ] Edit Distance (opcional)

### Implementaciones
- [ ] `practice/algorithms/dynamic_programming.py`
- [ ] Fibonacci (memoization)
- [ ] Fibonacci (tabulation)
- [ ] DP template

---

## 1️⃣2️⃣ Greedy Algorithms

### Conceptos
- [ ] Greedy choice property
- [ ] Optimal substructure
- [ ] Greedy vs DP

### Problemas (5-6)
- [ ] Maximum Subarray
- [ ] Jump Game
- [ ] Jump Game II
- [ ] Gas Station
- [ ] Hand of Straights

### Implementaciones
- [ ] `practice/algorithms/greedy.py`

---

## 1️⃣3️⃣ Bit Manipulation

### Conceptos
- [ ] AND, OR, XOR, NOT
- [ ] Left shift, Right shift
- [ ] Set bit, clear bit, toggle bit
- [ ] Count bits

### Problemas (4-5)
- [ ] Number of 1 Bits
- [ ] Counting Bits
- [ ] Reverse Bits
- [ ] Missing Number
- [ ] Sum of Two Integers

### Implementaciones
- [ ] `practice/algorithms/bit_manipulation.py`

---

## 1️⃣4️⃣ Math & Logic

### Conceptos
- [ ] Combinatorics (n choose k)
- [ ] Probability basics
- [ ] Prime numbers
- [ ] GCD, LCM
- [ ] Modular arithmetic

### Problemas (3-5)
- [ ] Happy Number
- [ ] Plus One
- [ ] Pow(x, n)
- [ ] Sqrt(x)

---

## 1️⃣5️⃣ Advanced Topics (Opcional)

### Trie
- [ ] Trie structure
- [ ] Insert, search, startsWith
- [ ] Implement Trie
- [ ] Design Add and Search Words Data Structure
- [ ] Word Search II

### Intervals
- [ ] Merge Intervals
- [ ] Insert Interval
- [ ] Non-overlapping Intervals
- [ ] Meeting Rooms
- [ ] Meeting Rooms II

### System Design (si aplica)
- [ ] Scalability concepts
- [ ] Load balancing
- [ ] Caching strategies
- [ ] Database design

---

## 🎯 Mock Interviews & Practice

### Google Warmup
- [ ] Sesión 1
- [ ] Sesión 2
- [ ] Sesión 3
- [ ] Sesión 4
- [ ] Sesión 5

### Mock Interviews
- [ ] Mock interview con Googler (gustavohar@google.com)
- [ ] Self mock interview (grabarse)
- [ ] Peer mock interview

### Behavioral Prep
- [ ] Preparar ejemplos de proyectos
- [ ] STAR method stories
- [ ] Preguntas sobre trade-offs

---

## 📚 Lectura de Libros

### Cracking the Coding Interview
- [ ] Cap. I - Arrays & Strings
- [ ] Cap. II - Linked Lists
- [ ] Cap. III - Stacks & Queues
- [ ] Cap. IV - Trees & Graphs
- [ ] Cap. VI - Big O
- [ ] Cap. VII - Technical Questions (estrategia)
- [ ] Cap. VIII - Recursion & DP
- [ ] Cap. IX - System Design (si aplica)
- [ ] Cap. X - Sorting & Searching

### Elements of Programming Interviews in Python
- [ ] Cap. 1-2 - Fundamentals
- [ ] Cap. 5 - Arrays
- [ ] Cap. 6 - Strings
- [ ] Cap. 7 - Linked Lists
- [ ] Cap. 8 - Stacks & Queues
- [ ] Cap. 9 - Binary Trees
- [ ] Cap. 12 - Hash Tables
- [ ] Cap. 16 - Recursion
- [ ] Cap. 17 - Dynamic Programming
- [ ] Cap. 18 - Graphs

### Fluent Python (Lectura complementaria)
- [ ] Cap. 2 - Data Structures
- [ ] Cap. 3 - Dictionaries
- [ ] Cap. 7 - Functions
- [ ] Cap. 17 - Iterators/Generators

---

## ✅ Pre-Interview Checklist

### Día Antes
- [ ] Revisar patrones clave
- [ ] Re-resolver 3 problemas favoritos
- [ ] Repasar Big O
- [ ] Dormir 8 horas

### Día de la Entrevista
- [ ] Probar cámara y micrófono
- [ ] Verificar internet estable
- [ ] Tener agua cerca
- [ ] Practicar Google Docs (sin IDE)
- [ ] Repasar "pensar en voz alta"
- [ ] Llegar 10 min antes

---

## 📊 Estadísticas de Progreso

### Problemas Resueltos
- **Easy**: ___ / 50 (objetivo)
- **Medium**: ___ / 45 (objetivo)
- **Hard**: ___ / 5 (objetivo)
- **Total**: ___ / 100

### Tiempo Invertido
- **Día 1**: ___ horas
- **Día 2**: ___ horas
- **Día 3**: ___ horas
- **Día 4**: ___ horas
- **Día 5**: ___ horas
- **Día 6**: ___ horas
- **Día 7**: ___ horas
- **Día 8**: ___ horas
- **Día 9**: ___ horas
- **Día 10**: ___ horas
- **Día 11**: ___ horas
- **Día 12**: ___ horas
- **Total**: ___ horas

### Confianza por Tópico (1-5)
- Big O: ___/5
- Arrays/Strings: ___/5
- Sorting/Searching: ___/5
- Hash Tables: ___/5
- Linked Lists: ___/5
- Stacks/Queues: ___/5
- Trees: ___/5
- Graphs: ___/5
- Heaps: ___/5
- Recursion: ___/5
- Dynamic Programming: ___/5
