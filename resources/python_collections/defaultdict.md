# defaultdict - Dictionary with Default Values

## What is defaultdict

defaultdict is a dictionary subclass that provides a default value for missing keys. When you access a key that doesn't exist, instead of raising a KeyError, it automatically creates the key with a default value produced by a factory function.

**Etymology:** The name "defaultdict" combines "default" (a predetermined value used when no other is specified) and "dict" (dictionary). It literally means "a dictionary that provides default values."

**Module:** `collections.defaultdict`

**Inherits from:** `dict`

---

## Brief History and Context

defaultdict was introduced in Python 2.5 as part of the `collections` module. Before its introduction, programmers had to manually check if keys existed before accessing them or use `dict.setdefault()`, which was verbose and error-prone. defaultdict eliminates this boilerplate by automatically initializing missing keys.

**Why it matters for interviews:** Graph problems, grouping data, and building complex data structures frequently require handling missing keys. Using defaultdict makes code cleaner and less error-prone, demonstrating knowledge of Python's standard library.

---

## Creating a defaultdict

### With built-in types as factory

```python
from collections import defaultdict

# Default value: 0 (int factory)
int_dict = defaultdict(int)
print(int_dict['missing'])  # 0
print(int_dict)
# defaultdict(<class 'int'>, {'missing': 0})

# Default value: [] (list factory)
list_dict = defaultdict(list)
list_dict['fruits'].append('apple')
print(list_dict['fruits'])  # ['apple']
print(list_dict)
# defaultdict(<class 'list'>, {'fruits': ['apple']})

# Default value: {} (dict factory)
dict_dict = defaultdict(dict)
dict_dict['person']['name'] = 'Alice'
print(dict_dict)
# defaultdict(<class 'dict'>, {'person': {'name': 'Alice'}})

# Default value: set() (set factory)
set_dict = defaultdict(set)
set_dict['tags'].add('python')
print(set_dict['tags'])  # {'python'}
```

---

### With lambda for custom defaults

```python
from collections import defaultdict

# Default value: -1
neg_dict = defaultdict(lambda: -1)
print(neg_dict['missing'])  # -1

# Default value: custom string
msg_dict = defaultdict(lambda: "Not found")
print(msg_dict['key'])  # "Not found"

# Default value: empty tuple
tuple_dict = defaultdict(lambda: ())
print(tuple_dict['key'])  # ()
```

---

### No factory (behaves like regular dict)

```python
from collections import defaultdict

# This will raise KeyError on missing keys
no_factory = defaultdict()
# print(no_factory['missing'])  # KeyError!
```

**Time Complexity:** O(1) for creation
**Space Complexity:** O(1)

---

## Core Operations

### 1. Accessing and inserting

**What it does:** Returns value for existing keys; creates and returns default for missing keys

**Conditions:** Factory must be callable with no arguments

**Big-O:**
- Time: O(1) average case
- Space: O(1) per new key

**Example:**

```python
from collections import defaultdict

# Counting occurrences
counter = defaultdict(int)
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']

for word in words:
    counter[word] += 1  # No need to check if key exists!

print(counter)
# defaultdict(<class 'int'>, {'apple': 3, 'banana': 2, 'cherry': 1})
```

---

### 2. Grouping data

**What it does:** Groups items by a key using list as default factory

**Conditions:** Use list factory for collecting multiple values per key

**Big-O:**
- Time: O(1) per append operation
- Space: O(n) for all grouped items

**Example:**

```python
from collections import defaultdict

# Group students by grade
students = [
    ('Alice', 'A'),
    ('Bob', 'B'),
    ('Charlie', 'A'),
    ('David', 'B'),
    ('Eve', 'A')
]

by_grade = defaultdict(list)
for name, grade in students:
    by_grade[grade].append(name)

print(by_grade)
# defaultdict(<class 'list'>, {
#     'A': ['Alice', 'Charlie', 'Eve'],
#     'B': ['Bob', 'David']
# })
```

---

### 3. Building adjacency lists (graphs)

**What it does:** Creates graph structure where each node maps to its neighbors

**Conditions:** Use list or set factory depending on whether edge order matters

**Big-O:**
- Time: O(1) per edge addition
- Space: O(V + E) where V is vertices, E is edges

**Example:**

```python
from collections import defaultdict

# Build undirected graph
graph = defaultdict(list)

edges = [(1, 2), (1, 3), (2, 3), (3, 4)]

for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)  # Undirected

print(graph)
# defaultdict(<class 'list'>, {
#     1: [2, 3],
#     2: [1, 3],
#     3: [1, 2, 4],
#     4: [3]
# })

# Accessing non-existent node doesn't crash
print(graph[999])  # []
```

---

### 4. Nested defaultdict

**What it does:** Creates multi-level dictionaries with automatic initialization

**Conditions:** Factory can be another defaultdict

**Big-O:**
- Time: O(1) per access at each level
- Space: O(n * m) for n keys and m nested keys

**Example:**

```python
from collections import defaultdict

# Two-level defaultdict
matrix = defaultdict(lambda: defaultdict(int))

matrix[0][0] = 1
matrix[0][1] = 2
matrix[5][10] = 99

print(matrix[0][0])   # 1
print(matrix[0][1])   # 2
print(matrix[5][10])  # 99
print(matrix[1][1])   # 0 (auto-created)

print(dict(matrix))
# {0: defaultdict(<class 'int'>, {0: 1, 1: 2}),
#  5: defaultdict(<class 'int'>, {10: 99}),
#  1: defaultdict(<class 'int'>, {1: 0})}
```

---

### 5. Converting to regular dict

**What it does:** Removes default factory behavior

**Conditions:** Useful for serialization or when you want to prevent auto-creation

**Big-O:**
- Time: O(n)
- Space: O(n)

**Example:**

```python
from collections import defaultdict

dd = defaultdict(int, {'a': 1, 'b': 2})

# Convert to regular dict
regular = dict(dd)
print(type(regular))  # <class 'dict'>

# Now accessing missing key raises KeyError
# print(regular['missing'])  # KeyError!
```

---

## Quick Reference Table

| Operation                  | Description                      | Time  | Returns     |
|----------------------------|----------------------------------|-------|-------------|
| `defaultdict(factory)`     | Create with factory function     | O(1)  | defaultdict |
| `dd[key]`                  | Get or create with default       | O(1)  | value       |
| `dd[key] = value`          | Set value                        | O(1)  | None        |
| `key in dd`                | Check existence (no auto-create) | O(1)  | bool        |
| `dd.items()`               | Get key-value pairs              | O(1)  | view        |
| `dict(dd)`                 | Convert to regular dict          | O(n)  | dict        |
| `dd.default_factory`       | Access factory function          | O(1)  | callable    |

---

## Cookbook: Common Patterns

### Pattern 1: Frequency counter

```python
from collections import defaultdict

def count_frequencies(items):
    freq = defaultdict(int)
    for item in items:
        freq[item] += 1
    return freq

words = ['apple', 'banana', 'apple', 'cherry']
print(count_frequencies(words))
# defaultdict(<class 'int'>, {'apple': 2, 'banana': 1, 'cherry': 1})
```

---

### Pattern 2: Group by property

```python
from collections import defaultdict

def group_by_length(words):
    groups = defaultdict(list)
    for word in words:
        groups[len(word)].append(word)
    return groups

words = ['a', 'ab', 'abc', 'bc', 'xy', 'xyz']
print(group_by_length(words))
# defaultdict(<class 'list'>, {
#     1: ['a'],
#     2: ['ab', 'bc', 'xy'],
#     3: ['abc', 'xyz']
# })
```

---

### Pattern 3: Inverted index

```python
from collections import defaultdict

def build_inverted_index(documents):
    index = defaultdict(set)
    for doc_id, text in enumerate(documents):
        for word in text.split():
            index[word].add(doc_id)
    return index

docs = [
    "the quick brown fox",
    "the lazy dog",
    "quick brown dogs"
]

index = build_inverted_index(docs)
print(index['quick'])  # {0, 2}
print(index['dog'])    # {1}
```

---

### Pattern 4: Accumulating values

```python
from collections import defaultdict

def sum_by_category(transactions):
    totals = defaultdict(float)
    for category, amount in transactions:
        totals[category] += amount
    return totals

transactions = [
    ('food', 50.0),
    ('transport', 20.0),
    ('food', 30.0),
    ('entertainment', 100.0),
    ('transport', 15.0)
]

print(sum_by_category(transactions))
# defaultdict(<class 'float'>, {
#     'food': 80.0,
#     'transport': 35.0,
#     'entertainment': 100.0
# })
```

---

### Pattern 5: Graph traversal with adjacency list

```python
from collections import defaultdict, deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result

# Build graph
graph = defaultdict(list)
edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]
for u, v in edges:
    graph[u].append(v)

print(bfs(graph, 0))
# [0, 1, 2, 3, 4]
```

---

### Pattern 6: Tree structure

```python
from collections import defaultdict

def build_tree(parent_child_pairs):
    tree = defaultdict(list)
    for parent, child in parent_child_pairs:
        tree[parent].append(child)
    return tree

pairs = [
    ('root', 'A'),
    ('root', 'B'),
    ('A', 'A1'),
    ('A', 'A2'),
    ('B', 'B1')
]

tree = build_tree(pairs)
print(tree)
# defaultdict(<class 'list'>, {
#     'root': ['A', 'B'],
#     'A': ['A1', 'A2'],
#     'B': ['B1']
# })
```

---

## Interview Traps and Edge Cases

### Trap 1: Using 'in' doesn't trigger default

```python
from collections import defaultdict

dd = defaultdict(int)

# This does NOT create the key
if 'missing' in dd:
    print("Found")
else:
    print("Not found")  # This prints

print(dd)
# defaultdict(<class 'int'>, {})

# But accessing it does
value = dd['missing']
print(dd)
# defaultdict(<class 'int'>, {'missing': 0})
```

---

### Trap 2: Mutable default values

```python
from collections import defaultdict

# WRONG: This reuses the same list!
# wrong_dd = defaultdict([])  # TypeError! Must be callable

# RIGHT: Use lambda or list (the class itself)
right_dd = defaultdict(list)
right_dd['a'].append(1)
right_dd['b'].append(2)

print(right_dd)
# defaultdict(<class 'list'>, {'a': [1], 'b': [2]})
```

---

### Trap 3: Factory must be callable

```python
from collections import defaultdict

# WRONG: Passing a value instead of a callable
# dd = defaultdict(0)  # TypeError!

# RIGHT: Pass the type (callable)
dd = defaultdict(int)  # Correct

# Or use lambda
dd = defaultdict(lambda: 0)  # Also correct
```

---

### Trap 4: Converting to dict for JSON

```python
from collections import defaultdict
import json

dd = defaultdict(list)
dd['fruits'].append('apple')

# This fails!
# json.dumps(dd)  # TypeError: Object of type defaultdict is not JSON serializable

# Convert to dict first
regular = dict(dd)
print(json.dumps(regular))
# '{"fruits": ["apple"]}'
```

---

### Trap 5: default_factory can be None

```python
from collections import defaultdict

dd = defaultdict(int)
dd['a'] = 1

# Disable default factory
dd.default_factory = None

print(dd['a'])  # 1 (existing key)
# print(dd['b'])  # KeyError! (now behaves like regular dict)
```

---

## defaultdict vs Alternatives

### When to use defaultdict

- Building graphs (adjacency lists)
- Grouping items by key
- Counting when you don't want to use Counter
- Need automatic initialization

### When to use regular dict

- Don't want automatic key creation
- Need explicit control over defaults
- Serializing to JSON (need explicit conversion)

### When to use Counter

- Specifically counting frequencies
- Need most_common() or arithmetic operations
- Want integer counts only

### When to use dict.setdefault()

- One-off default needed
- Don't want to import collections
- Less readable but no dependency

**Comparison:**

```python
from collections import defaultdict

# Using defaultdict
dd = defaultdict(list)
dd['key'].append('value')

# Using regular dict with setdefault
regular = {}
regular.setdefault('key', []).append('value')

# Using regular dict with check
regular2 = {}
if 'key' not in regular2:
    regular2['key'] = []
regular2['key'].append('value')

# All produce same result
print(dd)       # defaultdict(<class 'list'>, {'key': ['value']})
print(regular)  # {'key': ['value']}
print(regular2) # {'key': ['value']}
```

---

## Key Takeaway for Interviews

**Golden phrase:**

> "defaultdict eliminates KeyError exceptions by automatically initializing missing keys with a factory function, making it ideal for graphs, grouping, and accumulating data in O(1) time per operation."

**Mental model:**

Think of defaultdict as a dictionary with a safety net. When you access a missing key, instead of crashing, it calls a factory function to create a sensible default value.

**When to mention in interviews:**

- "I'll use defaultdict(list) to build the adjacency list for this graph."
- "A defaultdict(int) lets me count without checking if keys exist."
- "Using defaultdict here eliminates edge case handling for missing keys."

---

## Practice Problems

Problems where defaultdict shines:

1. Group Anagrams (LeetCode #49)
2. Clone Graph (LeetCode #133)
3. Course Schedule (LeetCode #207)
4. Word Pattern (LeetCode #290)
5. Find Duplicate Subtrees (LeetCode #652)
6. Accounts Merge (LeetCode #721)

---

**Last Updated:** February 7, 2026
