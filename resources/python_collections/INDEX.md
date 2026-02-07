# Python Interview Toolkit Reference

A comprehensive study guide for essential Python collections, data structures, built-in functions, and patterns commonly used in technical interviews at Google and other FAANG companies.

**Note:** While this started as a collections reference, it has been expanded to include any Python feature, function, or pattern that is crucial for coding interviews.

---

## Purpose

This reference guide provides in-depth coverage of Python's built-in collections that are fundamental for solving algorithmic problems efficiently. Each module includes conceptual explanations, complexity analysis, practical examples, and common patterns.

---

## Quick Access

**New to these concepts?** Start with [ESSENTIALS.md](ESSENTIALS.md) - a curated list of must-memorize functions and patterns.

**Reviewing for interview?** Jump to the cookbook sections of each guide.

---

## Contents

### Core Collections

#### 1. Counter
**File:** [counter.md](counter.md)

A specialized dictionary for counting hashable objects. Essential for frequency-based problems.

**Key concepts:**
- Frequency counting and manipulation
- Multiset operations
- Most common elements retrieval

**Common use cases:**
- Finding duplicates
- Character frequency in strings
- Top-K frequent elements

---

#### 2. defaultdict
**File:** [defaultdict.md](defaultdict.md)

A dictionary subclass that provides default values for missing keys, eliminating KeyError exceptions.

**Key concepts:**
- Default factory functions
- Grouping and aggregation
- Graph adjacency lists

**Common use cases:**
- Building graphs
- Grouping data by key
- Accumulating values

---

#### 3. heapq (Min Heap)
**File:** [heapq.md](heapq.md)

A binary heap implementation providing efficient priority queue operations.

**Key concepts:**
- Min-heap property
- Logarithmic insertions and deletions
- Top-K problems

**Common use cases:**
- Finding K largest/smallest elements
- Merge K sorted lists
- Sliding window median

---

### Core Python Features

#### 4. Slicing
**File:** [slicing.md](slicing.md)

Python's powerful syntax for extracting portions of sequences. Master this for string and list manipulation.

**Key concepts:**
- `[start:stop:step]` syntax
- Negative indices
- Reversing with `[::-1]`
- Slice assignment (lists only)

**Common use cases:**
- Array rotation
- Window sliding
- Palindrome checking
- String reversal

---

### Additional Data Structures and Utilities

**Coming soon (add as you encounter them):**
- `deque` - Double-ended queue for efficient append/pop from both ends
- `bisect` - Binary search and insertion into sorted lists
- `itertools` - Combinatoric iterators (permutations, combinations, product)
- `functools` - Higher-order functions (lru_cache, reduce)
- `zip`, `enumerate`, `map`, `filter` - Built-in iteration helpers
- String methods - Essential built-ins (split, join, strip, etc.)
- List/Dict/Set comprehensions - Pythonic patterns
- Sorting with custom keys - sorted(), list.sort(), key functions
- Set operations - Union, intersection, symmetric difference
- Binary search - Template and variations

**Remember:** Add new modules here as you discover them in practice problems. Each should follow the same format as existing guides.

---

## Study Approach

### For interviews

1. **Understand time complexity** - Know the Big-O of each operation
2. **Practice patterns** - Each structure has common patterns (cookbooks)
3. **Compare alternatives** - Know when to use each structure vs alternatives
4. **Edge cases** - Empty collections, single element, duplicates

### Reading order

If you are new to these structures:
1. Start with **Counter** (simplest, builds on dict)
2. Move to **defaultdict** (extends dict concept)
3. Finish with **heapq** (more complex, different paradigm)

If you are reviewing:
- Jump directly to the cookbook sections
- Focus on complexity tables
- Practice the "Interview Traps" sections

---

## Notation Used

Throughout these guides:

**Time Complexity:**
- `O(1)` - Constant time
- `O(log n)` - Logarithmic time
- `O(n)` - Linear time
- `O(n log n)` - Linearithmic time

**Space Complexity:**
- Additional memory beyond input

**Code Examples:**
```python
# Code blocks show executable Python
result = function(input)
# Output is shown as comments or print statements
```

---

## Quick Reference Table

| Structure     | Primary Use                | Key Operation    | Time      |
|---------------|----------------------------|------------------|-----------|
| Counter       | Frequency counting         | `counter[key]`   | O(1)      |
| defaultdict   | Grouping/Default values    | `d[key].append`  | O(1)      |
| heapq         | Priority queue/Top-K       | `heappush/pop`   | O(log n)  |
| Slicing       | Sequence extraction        | `lst[start:stop:step]` | O(k)      |

---

## Additional Resources

- Python official documentation: https://docs.python.org/3/library/collections.html
- heapq documentation: https://docs.python.org/3/library/heapq.html
- Big-O Cheat Sheet: https://www.bigocheatsheet.com/

---

**Last Updated:** February 7, 2026
**Status:** Active study material for Google interview preparation
