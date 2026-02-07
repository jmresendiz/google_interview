# heapq - Binary Heap Priority Queue

## What is heapq

heapq is a module that implements a binary min-heap data structure. A heap is a specialized tree-based data structure that maintains the property that the smallest element is always at the root (index 0). In Python, heaps are implemented using regular lists, making them memory-efficient and easy to use.

**Etymology:** The word "heap" comes from the Old English word meaning "pile" or "mound." In computer science, it refers to a tree structure where elements are organized in a specific order. The term evokes the idea of a pile where the smallest (or largest) item naturally rises to the top.

**Module:** `heapq` (built-in, no installation needed)

**Data structure:** Binary min-heap (smallest element is always at index 0)

---

## Brief History and Context

The heap data structure was first introduced by J.W.J. Williams in 1964 for the heapsort algorithm. Python's heapq module was added to the standard library in Python 2.3 (2003) and provides a min-heap implementation using a regular Python list.

Unlike many languages that provide both min-heap and max-heap, Python's heapq only implements min-heap. To use it as a max-heap, you must negate values or use tuples with negated priorities.

**Why it matters for interviews:** Heaps are essential for priority queue operations, finding top-K elements, merging sorted lists, and scheduling problems. They provide O(log n) insertion and deletion, making them far more efficient than sorting for these use cases.

**Critical understanding:** A heap is NOT a sorted list. It only guarantees that the minimum element is at position 0. The rest of the elements are partially ordered but not fully sorted.

---

## Understanding Heap Structure

### Visual representation

A heap is a complete binary tree stored as a list:

```
Array: [1, 3, 5, 4, 8, 7]

Tree representation:
        1
       / \
      3   5
     / \ /
    4  8 7
```

### Index relationships

For element at index `i`:
- Left child: `2*i + 1`
- Right child: `2*i + 2`
- Parent: `(i - 1) // 2`

### Min-heap property

Every parent is smaller than or equal to its children:
- `heap[i] <= heap[2*i + 1]` (left child)
- `heap[i] <= heap[2*i + 2]` (right child)

---

## Core Operations

### 1. heappush(heap, item)

**What it does:** Inserts an element into the heap while maintaining the heap property

**Conditions:**
- The heap can be empty
- The heap size increases by 1

**Big-O:**
- Time: O(log n)
- Space: O(1)

**How it works:** The new element is added at the end of the list, then "bubbled up" by swapping with its parent until the heap property is restored.

**Example:**

```python
import heapq

heap = []

# Insert elements
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)

print(heap)
# [1, 3, 7, 4]
# Note: Not sorted, but heap property maintained

print(f"Minimum element: {heap[0]}")
# Minimum element: 1
```

---

### 2. heappop(heap)

**What it does:** Removes and returns the smallest element from the heap

**Conditions:**
- The heap must NOT be empty (raises IndexError otherwise)

**Big-O:**
- Time: O(log n)
- Space: O(1)

**How it works:** The root (minimum) is removed, the last element is moved to the root, then "bubbled down" by swapping with the smaller child until heap property is restored.

**Example:**

```python
import heapq

heap = [1, 3, 7, 4]

min_elem = heapq.heappop(heap)
print(f"Removed: {min_elem}")
# Removed: 1

print(heap)
# [3, 4, 7]
# Heap property still maintained

# Attempting pop on empty heap
empty_heap = []
# heapq.heappop(empty_heap)  # IndexError: index out of range
```

---

### 3. heappushpop(heap, item)

**What it does:** Pushes item onto heap, then pops and returns the smallest element

**Conditions:**
- The heap can be empty
- More efficient than separate push and pop

**Big-O:**
- Time: O(log n)
- Space: O(1)

**Why use it:** When you need to maintain a fixed-size heap, this is more efficient than calling heappush followed by heappop.

**Example:**

```python
import heapq

heap = [2, 5, 8]

# Push 3, then pop minimum
result = heapq.heappushpop(heap, 3)

print(f"Returned: {result}")
# Returned: 2

print(heap)
# [3, 5, 8]

# If the new item is smallest, it's returned immediately
heap = [5, 7, 9]
result = heapq.heappushpop(heap, 1)

print(f"Returned: {result}")
# Returned: 1

print(heap)
# [5, 7, 9]
# Heap unchanged because 1 was smaller than everything
```

---

### 4. heapreplace(heap, item)

**What it does:** Pops the smallest element, then pushes the new item

**Conditions:**
- The heap must NOT be empty (raises IndexError otherwise)
- Always removes the minimum, even if the new item is smaller

**Big-O:**
- Time: O(log n)
- Space: O(1)

**Critical difference from heappushpop:** This ALWAYS removes the current minimum first, regardless of the new item's value.

**Use case:** Maintaining a fixed-size heap (Top-K problems)

**Example:**

```python
import heapq

heap = [1, 5, 10]

# Pop 1, then push 7
result = heapq.heapreplace(heap, 7)

print(f"Removed: {result}")
# Removed: 1

print(heap)
# [5, 7, 10]

# Important: It removes minimum even if new item is smaller!
heap = [5, 8, 10]
result = heapq.heapreplace(heap, 2)

print(f"Removed: {result}")
# Removed: 5 (not 2!)

print(heap)
# [2, 8, 10]
# The 2 was pushed AFTER 5 was removed
```

---

### 5. Peek at minimum (heap[0])

**What it does:** Returns the smallest element without modifying the heap

**Conditions:**
- Heap must not be empty

**Big-O:**
- Time: O(1)
- Space: O(1)

**Example:**

```python
import heapq

heap = [3, 5, 7, 9]

# Peek at minimum
min_val = heap[0]
print(f"Minimum: {min_val}")
# Minimum: 3

print(heap)
# [3, 5, 7, 9]
# Heap unchanged

# Safe peek with default
def peek(heap, default=None):
    return heap[0] if heap else default

print(peek([]))      # None
print(peek([], -1))  # -1
```

---

### 6. heapify(list)

**What it does:** Converts a list into a valid heap in-place

**Conditions:**
- Modifies the original list
- Much more efficient than repeated heappush

**Big-O:**
- Time: O(n) - This is surprisingly efficient!
- Space: O(1)

**Why O(n) not O(n log n):** The algorithm processes elements from bottom to top, so most elements only need small adjustments.

**Example:**

```python
import heapq

# Unordered list
arr = [5, 1, 10, 3, 8, 2]

print(f"Before heapify: {arr}")
# Before heapify: [5, 1, 10, 3, 8, 2]

# Convert to heap in-place
heapq.heapify(arr)

print(f"After heapify: {arr}")
# After heapify: [1, 3, 2, 5, 8, 10]

print(f"Minimum: {arr[0]}")
# Minimum: 1

# Now it's a valid heap
heapq.heappush(arr, 0)
print(arr)
# [0, 3, 1, 5, 8, 10, 2]
```

---

### 7. nlargest(n, iterable, key=None)

**What it does:** Returns the n largest elements in descending order

**Conditions:**
- More efficient than sorting when n is small relative to the total size
- Does NOT modify the original iterable

**Big-O:**
- Time: O(m log n) where m is the iterable size and n is the count
- Space: O(n)

**When to use:** When n << len(iterable), this is faster than sorting

**Example:**

```python
import heapq

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# Get 3 largest
largest = heapq.nlargest(3, numbers)
print(largest)
# [9, 6, 5]

# With key function
words = ['apple', 'pie', 'a', 'cherry', 'tart']
longest = heapq.nlargest(2, words, key=len)
print(longest)
# ['cherry', 'apple']

# With tuples
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
top_scores = heapq.nlargest(2, students, key=lambda x: x[1])
print(top_scores)
# [('Bob', 92), ('Alice', 85)]
```

---

### 8. nsmallest(n, iterable, key=None)

**What it does:** Returns the n smallest elements in ascending order

**Conditions:**
- More efficient than sorting when n is small
- Does NOT modify the original iterable

**Big-O:**
- Time: O(m log n) where m is the iterable size
- Space: O(n)

**Example:**

```python
import heapq

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# Get 3 smallest
smallest = heapq.nsmallest(3, numbers)
print(smallest)
# [1, 1, 2]

# With dictionary
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95}
lowest = heapq.nsmallest(2, scores.items(), key=lambda x: x[1])
print(lowest)
# [('Charlie', 78), ('Alice', 85)]
```

---

## Quick Reference Table

| Operation           | Description              | Time      | Modifies Heap | Returns      |
|---------------------|--------------------------|-----------|---------------|--------------|
| `heappush(h, x)`    | Insert element           | O(log n)  | Yes           | None         |
| `heappop(h)`        | Remove minimum           | O(log n)  | Yes           | min element  |
| `heappushpop(h, x)` | Push then pop            | O(log n)  | Yes           | min element  |
| `heapreplace(h, x)` | Pop then push            | O(log n)  | Yes           | old min      |
| `h[0]`              | Peek at minimum          | O(1)      | No            | min element  |
| `heapify(list)`     | Convert list to heap     | O(n)      | Yes           | None         |
| `nlargest(n, iter)` | Get n largest            | O(m log n)| No            | list         |
| `nsmallest(n, iter)`| Get n smallest           | O(m log n)| No            | list         |

---

## Comparison: When to Use What

### heappushpop vs heapreplace

```python
import heapq

# heappushpop: Push FIRST, then pop
heap = [5, 7, 9]
result = heapq.heappushpop(heap, 1)
# Returns: 1 (because 1 < 5)
# Heap: [5, 7, 9] (unchanged)

# heapreplace: Pop FIRST, then push
heap = [5, 7, 9]
result = heapq.heapreplace(heap, 1)
# Returns: 5 (old minimum)
# Heap: [1, 7, 9] (1 was added)
```

**Rule of thumb:**
- Use `heappushpop` when you want to keep the heap size constant and possibly reject the new element
- Use `heapreplace` when you always want to remove the current minimum

---

### nlargest/nsmallest vs sorting

```python
import heapq

data = list(range(1000000))

# For small n (n << len(data))
# nsmallest is MUCH faster
smallest_10 = heapq.nsmallest(10, data)  # O(n log 10) ≈ O(n)

# Sorting is slower
# sorted_data = sorted(data)[:10]  # O(n log n)

# But if n is large (n ≈ len(data))
# Sorting is better
# heapq.nsmallest(900000, data)  # Slower
# sorted(data)[:900000]           # Faster
```

**Rule of thumb:**
- Use `nlargest/nsmallest` when n < len(data) / 10
- Use `sorted()` when n is close to len(data)

---

## Cookbook: Common Patterns

### Pattern 1: Top K elements (most common interview pattern)

**Problem:** Find the K largest elements from a stream

```python
import heapq

def find_k_largest(nums, k):
    """
    Maintains a min-heap of size k.
    Smallest of the k largest is at the top.

    Time: O(n log k)
    Space: O(k)
    """
    heap = []

    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num > heap[0]:
            heapq.heapreplace(heap, num)

    return heap

nums = [3, 2, 1, 5, 6, 4]
print(find_k_largest(nums, 2))
# [5, 6]
```

---

### Pattern 2: Merge K sorted lists

**Problem:** Merge multiple sorted lists into one sorted list

```python
import heapq

def merge_k_sorted(lists):
    """
    Uses a min-heap to always get the smallest element.

    Time: O(n log k) where n is total elements, k is number of lists
    Space: O(k) for the heap
    """
    heap = []
    result = []

    # Initialize heap with first element from each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))  # (value, list_idx, elem_idx)

    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)

        # Add next element from same list
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))

    return result

lists = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

print(merge_k_sorted(lists))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

### Pattern 3: Running median

**Problem:** Find median of a stream of numbers

```python
import heapq

class MedianFinder:
    """
    Uses two heaps:
    - max_heap: stores smaller half (negated for max behavior)
    - min_heap: stores larger half

    Median is either max of max_heap or average of both tops.
    """

    def __init__(self):
        self.max_heap = []  # Left half (negated)
        self.min_heap = []  # Right half

    def add_num(self, num):
        # Add to max_heap first
        heapq.heappush(self.max_heap, -num)

        # Balance: ensure max_heap max <= min_heap min
        if self.max_heap and self.min_heap:
            if -self.max_heap[0] > self.min_heap[0]:
                val = -heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, val)

        # Balance sizes: max_heap can have at most 1 more element
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)

        if len(self.min_heap) > len(self.max_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)

    def find_median(self):
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2

# Usage
mf = MedianFinder()
mf.add_num(1)
mf.add_num(2)
print(mf.find_median())  # 1.5

mf.add_num(3)
print(mf.find_median())  # 2.0
```

---

### Pattern 4: Task scheduler with priorities

**Problem:** Schedule tasks based on priority

```python
import heapq

class TaskScheduler:
    def __init__(self):
        self.heap = []
        self.counter = 0  # For tie-breaking

    def add_task(self, priority, task_name):
        """Lower priority number = higher priority"""
        heapq.heappush(self.heap, (priority, self.counter, task_name))
        self.counter += 1

    def get_next_task(self):
        if not self.heap:
            return None
        priority, _, task_name = heapq.heappop(self.heap)
        return task_name

# Usage
scheduler = TaskScheduler()
scheduler.add_task(3, "Low priority task")
scheduler.add_task(1, "High priority task")
scheduler.add_task(2, "Medium priority task")

print(scheduler.get_next_task())  # High priority task
print(scheduler.get_next_task())  # Medium priority task
print(scheduler.get_next_task())  # Low priority task
```

---

### Pattern 5: Sliding window median

**Problem:** Find median in a sliding window

```python
import heapq
from collections import Counter

def sliding_window_median(nums, k):
    """
    Uses two heaps with lazy deletion.

    Time: O(n log k)
    Space: O(k)
    """
    max_heap = []  # Left half (negated)
    min_heap = []  # Right half
    removed = Counter()

    def add(num):
        if not max_heap or num <= -max_heap[0]:
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)

    def remove(num):
        removed[num] += 1

    def clean(heap):
        """Remove invalid elements from top"""
        while heap and removed[abs(heap[0])] > 0:
            removed[abs(heap[0])] -= 1
            heapq.heappop(heap)

    def balance():
        # Balance after cleaning
        while len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        while len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

    def get_median():
        clean(max_heap)
        clean(min_heap)
        if len(max_heap) > len(min_heap):
            return float(-max_heap[0])
        return (-max_heap[0] + min_heap[0]) / 2.0

    result = []

    # Initialize window
    for i in range(k):
        add(nums[i])
    balance()
    result.append(get_median())

    # Slide window
    for i in range(k, len(nums)):
        remove(nums[i - k])
        add(nums[i])
        balance()
        result.append(get_median())

    return result

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(sliding_window_median(nums, k))
# [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
```

---

### Pattern 6: Dijkstra's shortest path

**Problem:** Find shortest path in weighted graph

```python
import heapq
from collections import defaultdict

def dijkstra(graph, start):
    """
    Time: O((V + E) log V)
    Space: O(V)
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    heap = [(0, start)]  # (distance, node)
    visited = set()

    while heap:
        dist, node = heapq.heappop(heap)

        if node in visited:
            continue

        visited.add(node)

        for neighbor, weight in graph[node]:
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return distances

# Graph as adjacency list: node -> [(neighbor, weight)]
graph = defaultdict(list)
graph[0] = [(1, 4), (2, 1)]
graph[1] = [(3, 1)]
graph[2] = [(1, 2), (3, 5)]
graph[3] = []

print(dijkstra(graph, 0))
# {0: 0, 1: 3, 2: 1, 3: 4}
```

---

## Max-Heap Implementation

Python's heapq only provides min-heap. To use it as max-heap:

### Method 1: Negate values

```python
import heapq

# Max-heap using negation
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -7)

# Get maximum (negate back)
maximum = -heapq.heappop(max_heap)
print(maximum)  # 7

print([-x for x in max_heap])
# [5, 3]
```

### Method 2: Use tuples with negated priority

```python
import heapq

# Max-heap for objects
max_heap = []
heapq.heappush(max_heap, (-5, 'item1'))
heapq.heappush(max_heap, (-3, 'item2'))
heapq.heappush(max_heap, (-7, 'item3'))

priority, item = heapq.heappop(max_heap)
print(f"Max priority {-priority}: {item}")
# Max priority 7: item3
```

---

## Interview Traps and Edge Cases

### Trap 1: Heap is NOT fully sorted

```python
import heapq

heap = [1, 3, 5, 4, 8, 7, 6]
heapq.heapify(heap)

print(heap)
# [1, 3, 5, 4, 8, 7, 6]

# heap[1] is NOT necessarily the second smallest!
print(f"heap[0] = {heap[0]}")  # 1 (guaranteed minimum)
print(f"heap[1] = {heap[1]}")  # 3 (NOT guaranteed second smallest)

# To get sorted order, pop everything
sorted_vals = []
while heap:
    sorted_vals.append(heapq.heappop(heap))

print(sorted_vals)
# [1, 3, 4, 5, 6, 7, 8]
```

---

### Trap 2: heapreplace on empty heap crashes

```python
import heapq

heap = []

# This crashes!
# heapq.heapreplace(heap, 5)  # IndexError!

# Use heappushpop instead (safe on empty heap)
result = heapq.heappushpop(heap, 5)
print(result)  # 5
print(heap)    # []
```

---

### Trap 3: Tuples are compared element-by-element

```python
import heapq

# This can cause issues if second element is not comparable
heap = []
heapq.heappush(heap, (1, {'data': 'a'}))
# heapq.heappush(heap, (1, {'data': 'b'}))  # TypeError: '<' not supported

# Solution: Add tie-breaker
counter = 0
heap = []
heapq.heappush(heap, (1, counter, {'data': 'a'}))
counter += 1
heapq.heappush(heap, (1, counter, {'data': 'b'}))
counter += 1

print(heap)
# [(1, 0, {'data': 'a'}), (1, 1, {'data': 'b'})]
```

---

### Trap 4: heapify modifies in-place

```python
import heapq

original = [5, 1, 10, 3]
heap = original  # NOT a copy!

heapq.heapify(heap)

print(original)  # [1, 3, 10, 5] - MODIFIED!

# To preserve original
original = [5, 1, 10, 3]
heap = original[:]  # Create a copy
heapq.heapify(heap)

print(original)  # [5, 1, 10, 3] - Unchanged
print(heap)      # [1, 3, 10, 5]
```

---

### Trap 5: Don't peek at heap[1] or heap[2]

```python
import heapq

heap = [1, 5, 3, 9, 7, 8]
heapq.heapify(heap)

# WRONG: heap[1] is NOT the second smallest
print(f"heap[0] = {heap[0]}")  # 1 (correct minimum)
print(f"heap[1] = {heap[1]}")  # 5 (might not be second smallest)

# RIGHT: Pop twice to get two smallest
first = heapq.heappop(heap)
second = heapq.heappop(heap)

print(f"First: {first}, Second: {second}")
# First: 1, Second: 3
```

---

## Heap vs Alternatives

### When to use heap

- Need to repeatedly find/remove minimum (or maximum)
- Top-K problems where K << N
- Priority queue operations
- Merge K sorted lists
- Streaming data (median, percentiles)

### When to use sorted list

- Need all elements in sorted order
- Need to access elements by index
- K is close to N in Top-K problems

### When to use sorting

- One-time sorting operation
- Need full sorted order
- Simple comparison (heaps are harder to debug)

### When to use BST (not built-in)

- Need ordered iteration
- Frequent deletions of arbitrary elements
- Need to find successor/predecessor

---

## Performance Comparison

```python
import heapq
import time

# Finding top 100 from 1 million elements

data = list(range(1000000, 0, -1))

# Method 1: heapq.nsmallest
start = time.time()
result = heapq.nsmallest(100, data)
print(f"nsmallest: {time.time() - start:.4f}s")
# nsmallest: ~0.05s

# Method 2: Sort and slice
start = time.time()
result = sorted(data)[:100]
print(f"sorted: {time.time() - start:.4f}s")
# sorted: ~0.15s

# Method 3: Manual heap (for K=100, similar to nsmallest)
start = time.time()
heap = []
for num in data:
    if len(heap) < 100:
        heapq.heappush(heap, -num)  # Max heap
    elif num < -heap[0]:
        heapq.heapreplace(heap, -num)
result = sorted([-x for x in heap])
print(f"manual heap: {time.time() - start:.4f}s")
# manual heap: ~0.05s
```

---

## Key Takeaway for Interviews

**Golden phrase:**

> "Heap operations are logarithmic because they only traverse the height of the binary tree. For Top-K problems with K << N, maintaining a size-K heap gives O(N log K) time, much better than sorting's O(N log N)."

**Mental model:**

Think of a heap as a partially ordered tree where you only care about the minimum (or maximum). It's not fully sorted, but it guarantees you can always get the smallest element in O(1) time and remove it in O(log N) time.

**When to mention in interviews:**

- "I'll use a min-heap of size K to track the K largest elements in O(N log K) time."
- "A heap gives us O(log N) insertions instead of O(N) for maintaining sorted order."
- "For merging K sorted lists, a heap reduces time from O(NK log K) to O(NK log K) by always picking the minimum across lists."
- "The heapify operation is O(N), not O(N log N), because most elements are near the leaves."

---

## Practice Problems

Essential heap problems for Google interviews:

**Top-K pattern:**
1. Kth Largest Element in an Array (LeetCode #215)
2. Top K Frequent Elements (LeetCode #347)
3. K Closest Points to Origin (LeetCode #973)

**Merge pattern:**
4. Merge K Sorted Lists (LeetCode #23)
5. Find K Pairs with Smallest Sums (LeetCode #373)

**Median/Running median:**
6. Find Median from Data Stream (LeetCode #295)
7. Sliding Window Median (LeetCode #480)

**Graph/Scheduling:**
8. Meeting Rooms II (LeetCode #253)
9. Task Scheduler (LeetCode #621)
10. Cheapest Flights Within K Stops (LeetCode #787)

**Advanced:**
11. The Skyline Problem (LeetCode #218)
12. IPO (LeetCode #502)

---

**Last Updated:** February 7, 2026
