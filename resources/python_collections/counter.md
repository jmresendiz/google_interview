# Counter - Frequency Counting Dictionary

## What is Counter

Counter is a specialized dictionary subclass designed for counting hashable objects. It stores elements as dictionary keys and their counts as values. Unlike regular dictionaries, accessing a missing key returns 0 instead of raising a KeyError.

**Etymology:** The word "counter" comes from the verb "to count," meaning to enumerate or tally items. In programming, it refers to an object that maintains counts.

**Module:** `collections.Counter`

**Inherits from:** `dict`

---

## Brief History and Context

Counter was introduced in Python 2.7 and 3.1 as part of the `collections` module. It was designed to simplify frequency counting operations that previously required manual dictionary manipulation. This pattern is so common in data analysis and algorithmic problems that having a dedicated class significantly reduces boilerplate code.

**Why it matters for interviews:** Frequency counting is one of the most common patterns in coding interviews. Problems involving anagrams, duplicates, top-K elements, and character manipulation often benefit from Counter.

---

## Creating a Counter

### From an iterable

```python
from collections import Counter

# Count characters in a string
text = "mississippi"
char_count = Counter(text)
print(char_count)
# Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

# Count elements in a list
numbers = [1, 2, 2, 3, 3, 3]
num_count = Counter(numbers)
print(num_count)
# Counter({3: 3, 2: 2, 1: 1})
```

### From a dictionary

```python
freq = Counter({'a': 3, 'b': 1, 'c': 2})
print(freq)
# Counter({'a': 3, 'c': 2, 'b': 1})
```

### From keyword arguments

```python
counter = Counter(red=4, blue=2)
print(counter)
# Counter({'red': 4, 'blue': 2})
```

### Empty counter

```python
empty = Counter()
print(empty)
# Counter()
```

**Time Complexity:** O(n) where n is the number of elements to count
**Space Complexity:** O(k) where k is the number of unique elements

---

## Core Operations

### 1. Accessing counts

**What it does:** Returns the count for a given element

**Conditions:** Works even if the element doesn't exist (returns 0)

**Big-O:**
- Time: O(1)
- Space: O(1)

**Example:**

```python
from collections import Counter

counter = Counter(['a', 'b', 'c', 'a', 'b', 'a'])

print(counter['a'])  # 3
print(counter['b'])  # 2
print(counter['z'])  # 0 (not KeyError!)
```

---

### 2. most_common(n)

**What it does:** Returns a list of the n most common elements with their counts, ordered from most to least common

**Conditions:**
- If n is omitted, returns all elements
- If n is larger than the number of elements, returns all

**Big-O:**
- Time: O(n log k) where k is the number of unique elements
- Space: O(k)

**Example:**

```python
from collections import Counter

votes = Counter(['Alice', 'Bob', 'Alice', 'Charlie', 'Alice', 'Bob'])

# Get top 2
print(votes.most_common(2))
# [('Alice', 3), ('Bob', 2)]

# Get all (sorted by frequency)
print(votes.most_common())
# [('Alice', 3), ('Bob', 2), ('Charlie', 1)]
```

---

### 3. elements()

**What it does:** Returns an iterator over elements, repeating each as many times as its count

**Conditions:**
- Counts less than 1 are ignored
- Elements are returned in arbitrary order

**Big-O:**
- Time: O(n) where n is the sum of all counts
- Space: O(1) for iterator, O(n) if converted to list

**Example:**

```python
from collections import Counter

counter = Counter(a=3, b=1, c=0)

print(list(counter.elements()))
# ['a', 'a', 'a', 'b']
# Note: 'c' is not included (count is 0)
```

---

### 4. update()

**What it does:** Adds counts from an iterable or another counter (not replacement, addition)

**Conditions:**
- Can accept iterables, dictionaries, or other Counters
- Counts are added, not replaced

**Big-O:**
- Time: O(n) where n is the number of elements added
- Space: O(k) for new unique elements

**Example:**

```python
from collections import Counter

counter = Counter(['a', 'b', 'c'])
print(counter)
# Counter({'a': 1, 'b': 1, 'c': 1})

counter.update(['a', 'a', 'd'])
print(counter)
# Counter({'a': 3, 'b': 1, 'c': 1, 'd': 1})

# From another Counter
counter.update(Counter({'a': 1, 'e': 2}))
print(counter)
# Counter({'a': 4, 'e': 2, 'b': 1, 'c': 1, 'd': 1})
```

---

### 5. subtract()

**What it does:** Subtracts counts (can result in zero or negative counts)

**Conditions:**
- Unlike update, this subtracts instead of adding
- Negative counts are allowed

**Big-O:**
- Time: O(n)
- Space: O(k) for new unique elements

**Example:**

```python
from collections import Counter

counter = Counter(a=4, b=2, c=0)
counter.subtract(Counter(a=1, b=3))

print(counter)
# Counter({'a': 3, 'c': 0, 'b': -1})
```

---

### 6. Arithmetic Operations

**What it does:** Perform set-like operations with other Counters

**Supported operations:**
- Addition: `+` (combine counts)
- Subtraction: `-` (remove counts, keep only positive)
- Intersection: `&` (minimum counts)
- Union: `|` (maximum counts)

**Big-O:**
- Time: O(n + m) where n and m are the sizes of the Counters
- Space: O(n + m)

**Example:**

```python
from collections import Counter

c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2, c=1)

# Addition
print(c1 + c2)
# Counter({'a': 4, 'b': 3, 'c': 1})

# Subtraction (keeps only positive)
print(c1 - c2)
# Counter({'a': 2})

# Intersection (minimum)
print(c1 & c2)
# Counter({'a': 1, 'b': 1})

# Union (maximum)
print(c1 | c2)
# Counter({'a': 3, 'b': 2, 'c': 1})
```

---

## Quick Reference Table

| Operation           | Description                | Time      | Returns        |
|---------------------|----------------------------|-----------|----------------|
| `Counter(iterable)` | Create counter             | O(n)      | Counter        |
| `counter[key]`      | Get count                  | O(1)      | int            |
| `most_common(n)`    | Top n elements             | O(n log k)| list of tuples |
| `elements()`        | Iterator of elements       | O(1)      | iterator       |
| `update(iterable)`  | Add counts                 | O(n)      | None           |
| `subtract(iterable)`| Subtract counts            | O(n)      | None           |
| `c1 + c2`           | Combine counters           | O(n + m)  | Counter        |
| `c1 - c2`           | Remove counts              | O(n + m)  | Counter        |
| `c1 & c2`           | Intersection (min)         | O(n + m)  | Counter        |
| `c1 | c2`           | Union (max)                | O(n + m)  | Counter        |

---

## Cookbook: Common Patterns

### Pattern 1: Check if two strings are anagrams

```python
from collections import Counter

def are_anagrams(s1, s2):
    return Counter(s1) == Counter(s2)

print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))    # False
```

---

### Pattern 2: Find top K frequent elements

```python
from collections import Counter

def top_k_frequent(nums, k):
    counter = Counter(nums)
    return [num for num, _ in counter.most_common(k)]

nums = [1, 1, 1, 2, 2, 3]
print(top_k_frequent(nums, 2))
# [1, 2]
```

---

### Pattern 3: Count characters and filter

```python
from collections import Counter

text = "Hello World"
counter = Counter(text.lower())

# Get only letters that appear more than once
duplicates = {char: count for char, count in counter.items()
              if char.isalpha() and count > 1}

print(duplicates)
# {'l': 3, 'o': 2}
```

---

### Pattern 4: Remove elements with zero or negative counts

```python
from collections import Counter

counter = Counter(a=3, b=0, c=-1, d=2)

# Clean up non-positive counts
counter = +counter  # Unary plus removes non-positive

print(counter)
# Counter({'a': 3, 'd': 2})
```

---

### Pattern 5: Find elements that appear exactly once

```python
from collections import Counter

def find_unique(nums):
    counter = Counter(nums)
    return [num for num, count in counter.items() if count == 1]

nums = [1, 2, 2, 3, 4, 4, 5]
print(find_unique(nums))
# [1, 3, 5]
```

---

### Pattern 6: Checking if string can form palindrome

```python
from collections import Counter

def can_form_palindrome(s):
    """A string can form a palindrome if at most one character has odd count"""
    counter = Counter(s)
    odd_count = sum(1 for count in counter.values() if count % 2 == 1)
    return odd_count <= 1

print(can_form_palindrome("civic"))      # True
print(can_form_palindrome("racecar"))    # True
print(can_form_palindrome("hello"))      # False
```

---

## Interview Traps and Edge Cases

### Trap 1: Counter does not raise KeyError

```python
from collections import Counter

counter = Counter(['a', 'b'])

# This does NOT raise an error
print(counter['z'])  # 0

# Regular dict would raise KeyError
regular_dict = {'a': 1, 'b': 1}
# print(regular_dict['z'])  # KeyError!
```

---

### Trap 2: Negative counts are allowed

```python
from collections import Counter

counter = Counter(a=2, b=1)
counter.subtract(Counter(a=5, b=1))

print(counter)
# Counter({'b': 0, 'a': -3})

# But arithmetic operations remove non-positive
result = Counter(a=2) - Counter(a=5)
print(result)
# Counter() - empty!
```

---

### Trap 3: elements() returns iterator, not list

```python
from collections import Counter

counter = Counter(a=2, b=1)

# This is an iterator
elems = counter.elements()
print(elems)
# <itertools.chain object at 0x...>

# Convert to list to see values
print(list(counter.elements()))
# ['a', 'a', 'b']
```

---

### Trap 4: most_common() returns list of tuples

```python
from collections import Counter

counter = Counter(['a', 'a', 'b'])

# Returns tuples, not just keys
top = counter.most_common(1)
print(top)
# [('a', 2)]

# Extract just the key
print(top[0][0])
# 'a'
```

---

## Counter vs Alternatives

### When to use Counter

- Frequency counting of hashable elements
- Need to find most/least common elements
- Need to perform multiset operations

### When to use regular dict

- Need more control over default values
- Don't need frequency-specific operations
- Building complex nested structures

### When to use defaultdict

- Need non-zero default values
- Building graphs or grouping data
- Default value is not an integer

---

## Key Takeaway for Interviews

**Golden phrase:**

> "Counter is a specialized dictionary for frequency counting that returns zero for missing keys and provides efficient most_common() for finding top elements in O(n log k) time."

**Mental model:**

Think of Counter as a dictionary with built-in counting superpowers. It handles all the bookkeeping of incrementing values and provides convenience methods for the most common frequency-based operations.

**When to mention in interviews:**

- "I'll use a Counter to track character frequencies in O(n) time and O(k) space."
- "Counter's most_common() gives us the top K elements efficiently."
- "Since we need frequency counting, Counter is cleaner than manually managing a dict."

---

## Practice Problems

Problems where Counter shines:

1. Valid Anagram (LeetCode #242)
2. Top K Frequent Elements (LeetCode #347)
3. First Unique Character in a String (LeetCode #387)
4. Sort Characters By Frequency (LeetCode #451)
5. Find All Anagrams in a String (LeetCode #438)

---

**Last Updated:** February 7, 2026
