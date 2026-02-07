# Essential Python Patterns - Must Memorize

This guide contains the most critical Python patterns, functions, and idioms you should have memorized for technical interviews. These are patterns that appear in 80% of interview problems.

**Study approach:** Memorize the time complexity and basic usage. Practice writing these from memory without looking up documentation.

---

## Collections Module

### Counter

**Import:**
```python
from collections import Counter
```

**Critical operations:**

| Operation | Code | Time | Use Case |
|-----------|------|------|----------|
| Create | `Counter(iterable)` | O(n) | Frequency counting |
| Access | `counter[key]` | O(1) | Get count (returns 0 if missing) |
| Top K | `counter.most_common(k)` | O(n log k) | Find K most frequent |
| Iterate | `for k, v in counter.items()` | O(n) | Process all frequencies |

**Memorize:**
- Returns 0 for missing keys (no KeyError)
- `most_common()` returns list of tuples: `[(elem, count), ...]`

---

### defaultdict

**Import:**
```python
from collections import defaultdict
```

**Critical patterns:**

| Pattern | Code | Use Case |
|---------|------|----------|
| Count | `defaultdict(int)` | Frequency counting |
| Group | `defaultdict(list)` | Grouping items by key |
| Graph | `defaultdict(list)` | Adjacency list |
| Nested | `defaultdict(lambda: defaultdict(int))` | 2D sparse matrix |

**Memorize:**
- Factory is called ONLY when key doesn't exist
- Use `in` to check without creating key
- Convert to dict before JSON serialization

---

### heapq (Min Heap)

**Import:**
```python
import heapq
```

**Critical operations:**

| Operation | Code | Time | Memorize |
|-----------|------|------|----------|
| Create | `heapify(list)` | O(n) | In-place, modifies original |
| Insert | `heappush(heap, item)` | O(log n) | Maintains heap property |
| Remove min | `heappop(heap)` | O(log n) | Raises error if empty |
| Peek min | `heap[0]` | O(1) | Just access, don't pop |
| Push+Pop | `heappushpop(heap, item)` | O(log n) | More efficient than separate |
| Pop+Push | `heapreplace(heap, item)` | O(log n) | Heap must not be empty |

**Top-K pattern (MEMORIZE THIS):**
```python
# K largest: maintain min-heap of size K
heap = []
for num in nums:
    if len(heap) < k:
        heappush(heap, num)
    elif num > heap[0]:
        heapreplace(heap, num)
# heap contains K largest
```

**Max-heap pattern:**
```python
# Negate values for max-heap
heappush(heap, -value)
max_val = -heappop(heap)
```

---

### deque (Double-ended queue)

**Import:**
```python
from collections import deque
```

**Critical operations:**

| Operation | Code | Time | Use Case |
|-----------|------|------|----------|
| Create | `deque([1, 2, 3])` | O(n) | From iterable |
| Append right | `dq.append(x)` | O(1) | Add to end |
| Append left | `dq.appendleft(x)` | O(1) | Add to front |
| Pop right | `dq.pop()` | O(1) | Remove from end |
| Pop left | `dq.popleft()` | O(1) | Remove from front |
| Peek | `dq[0]`, `dq[-1]` | O(1) | First/last element |

**When to use:** Sliding window, BFS queue, maintaining order with efficient front/back access

**Memorize:** deque is better than list for pop(0) which is O(n) in list vs O(1) in deque

---

## Built-in Functions

### sorted() and list.sort()

**Critical patterns:**

```python
# Basic sorting
sorted(lst)                          # O(n log n), returns new list
lst.sort()                           # O(n log n), in-place

# Custom key function (CRITICAL)
sorted(lst, key=lambda x: x[1])      # Sort by second element
sorted(lst, key=lambda x: (x[0], -x[1]))  # Multi-level: ascending then descending
sorted(words, key=len)               # Sort by length
sorted(strs, key=str.lower)          # Case-insensitive

# Reverse
sorted(lst, reverse=True)            # Descending order
```

**Memorize:**
- `sorted()` creates new list, `sort()` modifies in-place
- Key function is called once per element
- Use tuples in key for multi-level sorting

---

### enumerate()

**Pattern:**
```python
for i, val in enumerate(lst):
    # i is index, val is value

# Start from different index
for i, val in enumerate(lst, start=1):
    # i starts at 1
```

**When to use:** Need both index and value in loop

---

### zip()

**Pattern:**
```python
# Combine two lists
for a, b in zip(list1, list2):
    # Stops at shortest list

# Unzip (transpose)
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
nums, letters = zip(*pairs)
# nums = (1, 2, 3), letters = ('a', 'b', 'c')
```

**Memorize:** `zip(*list)` transposes list of tuples

---

### map() and filter()

**Pattern:**
```python
# Map: apply function to all elements
nums = list(map(int, ['1', '2', '3']))
# nums = [1, 2, 3]

# Filter: keep elements where function returns True
evens = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))
# evens = [2, 4]
```

**Note:** Often list comprehensions are more Pythonic

---

### any() and all()

**Pattern:**
```python
# any: True if at least one is True
any([False, False, True])   # True
any([False, False])         # False

# all: True if all are True
all([True, True, True])     # True
all([True, False, True])    # False

# Common use with generators
any(x > 10 for x in nums)
all(x >= 0 for x in nums)
```

**Memorize:** Short-circuits (stops as soon as answer is known)

---

## String Methods

**Critical operations (MEMORIZE):**

```python
s = "  Hello, World!  "

# Splitting
s.split()           # Split on whitespace: ['Hello,', 'World!']
s.split(',')        # Split on delimiter: ['  Hello', ' World!  ']

# Joining
' '.join(['a', 'b', 'c'])  # 'a b c'
''.join(['a', 'b', 'c'])   # 'abc'

# Trimming
s.strip()           # Remove leading/trailing whitespace
s.lstrip()          # Left only
s.rstrip()          # Right only

# Case
s.lower()           # All lowercase
s.upper()           # All uppercase
s.capitalize()      # First char uppercase

# Checking
s.isalpha()         # All alphabetic
s.isdigit()         # All digits
s.isalnum()         # Alphanumeric
s.startswith('He')  # Starts with substring
s.endswith('!')     # Ends with substring

# Finding
s.find('World')     # Index of substring (or -1)
s.index('World')    # Index of substring (or ValueError)
'x' in s            # Contains check (True/False)
```

**Memorize:** Strings are immutable - all methods return new string

---

## List/Dict/Set Comprehensions

**List comprehension:**
```python
# Basic
[x * 2 for x in range(5)]
# [0, 2, 4, 6, 8]

# With condition
[x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

# Nested
[[i * j for j in range(3)] for i in range(3)]
# [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
```

**Dict comprehension:**
```python
{x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# From two lists
{k: v for k, v in zip(keys, values)}
```

**Set comprehension:**
```python
{x % 3 for x in range(10)}
# {0, 1, 2}
```

**Memorize:** Often faster and more readable than loops

---

## Set Operations

**Critical operations:**

```python
a = {1, 2, 3}
b = {2, 3, 4}

# Union (all elements)
a | b               # {1, 2, 3, 4}
a.union(b)

# Intersection (common elements)
a & b               # {2, 3}
a.intersection(b)

# Difference (in a but not in b)
a - b               # {1}
a.difference(b)

# Symmetric difference (in a or b but not both)
a ^ b               # {1, 4}
a.symmetric_difference(b)

# Subset/Superset
a <= b              # a is subset of b
a >= b              # a is superset of b
```

**Memorize:** All operations are O(n) on average

---

## Slicing

**Pattern:**
```python
lst = [0, 1, 2, 3, 4, 5]

# Basic slicing: lst[start:end:step]
lst[1:4]        # [1, 2, 3] (end not included)
lst[:3]         # [0, 1, 2] (from start)
lst[3:]         # [3, 4, 5] (to end)
lst[:]          # [0, 1, 2, 3, 4, 5] (copy)

# Negative indices
lst[-2:]        # [4, 5] (last two)
lst[:-2]        # [0, 1, 2, 3] (all except last two)

# Step
lst[::2]        # [0, 2, 4] (every other)
lst[::-1]       # [5, 4, 3, 2, 1, 0] (reverse)

# Strings work the same
s = "hello"
s[::-1]         # "olleh"
```

**Memorize:** `[start:end:step]` - end is exclusive

---

## Common Patterns (MUST KNOW)

### Two Pointers

```python
# Opposite ends
left, right = 0, len(arr) - 1
while left < right:
    # Process arr[left] and arr[right]
    if condition:
        left += 1
    else:
        right -= 1

# Same direction
slow = fast = 0
while fast < len(arr):
    # Move fast
    fast += 1
    # Maybe move slow
    if condition:
        slow += 1
```

---

### Sliding Window

```python
# Fixed size
window_size = k
for i in range(len(arr) - k + 1):
    window = arr[i:i+k]
    # Process window

# Variable size
left = 0
for right in range(len(arr)):
    # Expand window
    add_to_window(arr[right])

    # Shrink if needed
    while window_invalid():
        remove_from_window(arr[left])
        left += 1

    # Process current window
```

---

### Fast and Slow Pointers (Cycle Detection)

```python
# Floyd's algorithm
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        # Cycle detected
        break
```

---

### Binary Search

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Not found
```

**Memorize:** `left <= right`, not `left < right`

---

### DFS (Recursion)

```python
def dfs(node, visited):
    if node in visited:
        return

    visited.add(node)

    for neighbor in graph[node]:
        dfs(neighbor, visited)
```

---

### BFS (Queue)

```python
from collections import deque

def bfs(start):
    queue = deque([start])
    visited = {start}

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

**Memorize:** Use `deque` for BFS, not list (popleft is O(1))

---

## Time Complexities to Memorize

### List operations

| Operation | Time |
|-----------|------|
| `lst.append(x)` | O(1) amortized |
| `lst.pop()` | O(1) |
| `lst.pop(0)` | O(n) - avoid! |
| `lst.insert(0, x)` | O(n) - avoid! |
| `x in lst` | O(n) |
| `lst[i]` | O(1) |
| `lst.sort()` | O(n log n) |

---

### Dict operations

| Operation | Time |
|-----------|------|
| `d[key]` | O(1) average |
| `d[key] = val` | O(1) average |
| `key in d` | O(1) average |
| `del d[key]` | O(1) average |

---

### Set operations

| Operation | Time |
|-----------|------|
| `x in s` | O(1) average |
| `s.add(x)` | O(1) average |
| `s.remove(x)` | O(1) average |
| `s1 & s2` (intersection) | O(min(len(s1), len(s2))) |

---

## Interview Cheat Sheet

**Before writing code:**
1. Clarify the problem (edge cases, constraints)
2. Think about data structure choice
3. Estimate time/space complexity
4. Consider edge cases

**Common edge cases:**
- Empty input (`[]`, `""`, `{}`)
- Single element
- All same elements
- Negative numbers
- Very large numbers (overflow in other languages, but Python handles this)
- Duplicates
- Already sorted input

**Complexity goals:**
- Better than O(n²) for most problems
- O(n log n) is often acceptable (sorting)
- O(n) with O(n) space is usually better than O(n²) with O(1) space

**Communication:**
- Think out loud
- Explain your approach before coding
- Test with examples
- Walk through your code

---

## Practice Approach

1. **Memorize this entire file** - Write code from memory
2. **Recognize patterns** - Know when to use each structure
3. **Practice daily** - Use these in actual problems
4. **Build muscle memory** - Don't look up basic syntax during practice

**Test yourself:** Can you write these without looking?
- Binary search
- BFS with deque
- DFS recursive
- Two pointers for palindrome
- Sliding window max
- Top K with heap

If not, practice until you can.

---

**Last Updated:** February 7, 2026
**Status:** Core reference - review before every practice session
