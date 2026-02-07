# Python Slicing - Complete Reference

## What is Slicing

Slicing is a powerful Python feature that allows you to extract portions of sequences (lists, tuples, strings) using a concise syntax. It returns a new sequence without modifying the original.

**Etymology:** The word "slice" comes from the verb meaning "to cut into parts." In programming, it refers to extracting a portion of a sequence.

**Syntax:** `sequence[start:stop:step]`

**Applies to:** Lists, tuples, strings, and any object that implements `__getitem__`

---

## Basic Syntax

### The three parameters

```python
sequence[start:stop:step]
```

- **start:** Index where slice begins (inclusive)
- **stop:** Index where slice ends (exclusive)
- **step:** Increment between indices (default is 1)

**All parameters are optional:**
- `[:]` - entire sequence
- `[start:]` - from start to end
- `[:stop]` - from beginning to stop
- `[::step]` - entire sequence with step

---

## Basic Examples

### Lists

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing
print(numbers[2:5])
# [2, 3, 4]
# Indices 2, 3, 4 (stop=5 is exclusive)

print(numbers[0:3])
# [0, 1, 2]

print(numbers[5:8])
# [5, 6, 7]
```

---

### Strings

```python
text = "Hello, World!"

print(text[0:5])
# "Hello"

print(text[7:12])
# "World"

# Works exactly like lists
print(text[7:12] == list(text)[7:12])
# True (conceptually)
```

---

### Tuples

```python
coords = (0, 10, 20, 30, 40, 50)

print(coords[1:4])
# (10, 20, 30)

# Returns a new tuple
print(type(coords[1:4]))
# <class 'tuple'>
```

---

## Omitting Parameters

### Omitting start (defaults to 0)

```python
lst = [0, 1, 2, 3, 4, 5]

print(lst[:3])
# [0, 1, 2]
# Same as lst[0:3]

print(lst[:4])
# [0, 1, 2, 3]
```

---

### Omitting stop (goes to end)

```python
lst = [0, 1, 2, 3, 4, 5]

print(lst[3:])
# [3, 4, 5]
# From index 3 to end

print(lst[2:])
# [2, 3, 4, 5]
```

---

### Omitting both (copies entire sequence)

```python
lst = [0, 1, 2, 3, 4, 5]

print(lst[:])
# [0, 1, 2, 3, 4, 5]

# Creates a shallow copy
copy = lst[:]
copy[0] = 999

print(lst)
# [0, 1, 2, 3, 4, 5] (unchanged)

print(copy)
# [999, 1, 2, 3, 4, 5]
```

---

## Negative Indices

**Negative indices count from the end:**
- `-1` is the last element
- `-2` is the second-to-last
- `-n` is the nth element from the end

### Using negative indices

```python
lst = [0, 1, 2, 3, 4, 5]
#      0  1  2  3  4  5  (positive indices)
#     -6 -5 -4 -3 -2 -1  (negative indices)

# Last element
print(lst[-1])
# 5

# Last three elements
print(lst[-3:])
# [3, 4, 5]

# All except last two
print(lst[:-2])
# [0, 1, 2, 3]

# From second to second-to-last
print(lst[1:-1])
# [1, 2, 3, 4]
```

---

### Mixing positive and negative

```python
lst = [0, 1, 2, 3, 4, 5]

# From index 2 to second-to-last
print(lst[2:-1])
# [2, 3, 4]

# From third-to-last to index 4
print(lst[-3:4])
# [3]

# From third-to-last to end
print(lst[-3:])
# [3, 4, 5]
```

---

## Step Parameter

### Positive step

```python
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Every other element
print(lst[::2])
# [0, 2, 4, 6, 8]

# Every third element
print(lst[::3])
# [0, 3, 6, 9]

# From index 1, every 2 elements
print(lst[1::2])
# [1, 3, 5, 7, 9]

# Slice with start, stop, and step
print(lst[2:8:2])
# [2, 4, 6]
# Indices 2, 4, 6 (stops before 8)
```

---

### Negative step (reverse)

**Critical:** When step is negative, you're going backwards!

```python
lst = [0, 1, 2, 3, 4, 5]

# Reverse entire list
print(lst[::-1])
# [5, 4, 3, 2, 1, 0]

# Every other element, reversed
print(lst[::-2])
# [5, 3, 1]

# From index 4 to 1, backwards
print(lst[4:1:-1])
# [4, 3, 2]
# Start at 4, go backwards, stop before 1

# Entire list backwards
print(lst[::-1])
# [5, 4, 3, 2, 1, 0]
```

---

### Understanding negative step

**Key insight:** When step is negative:
- `start` should be greater than `stop`
- You're moving from right to left

```python
lst = [0, 1, 2, 3, 4, 5]

# WRONG: start < stop with negative step
print(lst[1:4:-1])
# [] (empty!)
# Can't go backwards from 1 to 4

# RIGHT: start > stop with negative step
print(lst[4:1:-1])
# [4, 3, 2]
# Goes backwards from 4 to 2 (stops before 1)

# Full reverse (omit start and stop)
print(lst[::-1])
# [5, 4, 3, 2, 1, 0]
```

---

## Common Patterns

### Pattern 1: Get first N elements

```python
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

n = 3
first_n = lst[:n]
print(first_n)
# [0, 1, 2]

# Works even if n > len(lst)
n = 100
print(lst[:n])
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] (all elements, no error)
```

---

### Pattern 2: Get last N elements

```python
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

n = 3
last_n = lst[-n:]
print(last_n)
# [7, 8, 9]

# Edge case: n = 0
print(lst[-0:])  # lst[0:]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] (entire list!)

# Safe version
def last_n_elements(lst, n):
    return lst[-n:] if n > 0 else []

print(last_n_elements(lst, 0))
# []
```

---

### Pattern 3: Remove first N elements

```python
lst = [0, 1, 2, 3, 4, 5]

n = 2
rest = lst[n:]
print(rest)
# [2, 3, 4, 5]
```

---

### Pattern 4: Remove last N elements

```python
lst = [0, 1, 2, 3, 4, 5]

n = 2
without_last = lst[:-n]
print(without_last)
# [0, 1, 2, 3]

# Edge case: n = 0
print(lst[:-0])
# [] (empty!)

# Safe version
def remove_last_n(lst, n):
    return lst[:-n] if n > 0 else lst[:]

print(remove_last_n(lst, 0))
# [0, 1, 2, 3, 4, 5]
```

---

### Pattern 5: Reverse a sequence

```python
# String
s = "hello"
print(s[::-1])
# "olleh"

# List
lst = [1, 2, 3, 4, 5]
print(lst[::-1])
# [5, 4, 3, 2, 1]

# Check if palindrome
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False
```

---

### Pattern 6: Every Nth element

```python
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Every 2nd element
print(lst[::2])
# [0, 2, 4, 6, 8]

# Every 3rd element
print(lst[::3])
# [0, 3, 6, 9]

# Every 2nd element starting from index 1
print(lst[1::2])
# [1, 3, 5, 7, 9]
```

---

### Pattern 7: Middle portion

```python
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Middle half
mid_start = len(lst) // 4
mid_end = 3 * len(lst) // 4

print(lst[mid_start:mid_end])
# [2, 3, 4, 5, 6, 7]

# Center element(s)
mid = len(lst) // 2
print(lst[mid-1:mid+1])
# [4, 5]
```

---

## Slice Assignment (Lists Only)

**Important:** Slice assignment works only for mutable sequences (lists), not strings or tuples.

### Replace elements

```python
lst = [0, 1, 2, 3, 4, 5]

# Replace middle elements
lst[2:4] = [20, 30]
print(lst)
# [0, 1, 20, 30, 4, 5]

# Replace with different length
lst[1:3] = [10, 11, 12, 13]
print(lst)
# [0, 10, 11, 12, 13, 30, 4, 5]
```

---

### Delete elements

```python
lst = [0, 1, 2, 3, 4, 5]

# Delete using empty list
lst[2:4] = []
print(lst)
# [0, 1, 4, 5]

# Or use del
del lst[1:3]
print(lst)
# [0, 5]
```

---

### Insert elements

```python
lst = [0, 1, 2, 3]

# Insert at index 2 (start=stop)
lst[2:2] = [10, 11]
print(lst)
# [0, 1, 10, 11, 2, 3]
```

---

## Interview Patterns

### Pattern 1: Rotate array

```python
def rotate_right(lst, k):
    """Rotate list k positions to the right"""
    k = k % len(lst)  # Handle k > len(lst)
    return lst[-k:] + lst[:-k]

lst = [1, 2, 3, 4, 5]
print(rotate_right(lst, 2))
# [4, 5, 1, 2, 3]

def rotate_left(lst, k):
    """Rotate list k positions to the left"""
    k = k % len(lst)
    return lst[k:] + lst[:k]

print(rotate_left(lst, 2))
# [3, 4, 5, 1, 2]
```

---

### Pattern 2: Split at index

```python
def split_at(lst, index):
    """Split list into two parts at index"""
    return lst[:index], lst[index:]

lst = [1, 2, 3, 4, 5]
left, right = split_at(lst, 3)

print(left)   # [1, 2, 3]
print(right)  # [4, 5]
```

---

### Pattern 3: Window sliding

```python
def sliding_windows(lst, window_size):
    """Generate all windows of given size"""
    return [lst[i:i+window_size] for i in range(len(lst) - window_size + 1)]

lst = [1, 2, 3, 4, 5]
windows = sliding_windows(lst, 3)

print(windows)
# [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
```

---

### Pattern 4: Palindrome checking

```python
def is_palindrome(s):
    # Remove non-alphanumeric and lowercase
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))
# True

print(is_palindrome("race a car"))
# False
```

---

### Pattern 5: Get all but first and last

```python
lst = [1, 2, 3, 4, 5]

middle = lst[1:-1]
print(middle)
# [2, 3, 4]

# Edge case: less than 3 elements
short = [1, 2]
print(short[1:-1])
# [] (empty)
```

---

## Edge Cases and Pitfalls

### Pitfall 1: Indices out of range don't error

```python
lst = [1, 2, 3]

# These DON'T raise errors
print(lst[10:20])
# []

print(lst[:100])
# [1, 2, 3]

print(lst[-100:])
# [1, 2, 3]

# But single index access DOES error
# print(lst[10])  # IndexError!
```

---

### Pitfall 2: Empty slice with -0

```python
lst = [1, 2, 3, 4, 5]

# -0 is the same as 0!
print(lst[:-0])
# [] (NOT the entire list!)

print(lst[-0:])
# [1, 2, 3, 4, 5] (entire list)
```

---

### Pitfall 3: Shallow copy vs deep copy

```python
original = [[1, 2], [3, 4]]

# Shallow copy
copy = original[:]

copy[0][0] = 999
print(original)
# [[999, 2], [3, 4]] (MODIFIED!)

# For nested structures, use copy.deepcopy
import copy
deep_copy = copy.deepcopy(original)
deep_copy[0][0] = 111

print(original)
# [[999, 2], [3, 4]] (unchanged by deep_copy modification)
```

---

### Pitfall 4: Step cannot be zero

```python
lst = [1, 2, 3]

# This raises ValueError
# print(lst[::0])  # ValueError: slice step cannot be zero
```

---

## Slicing vs Other Methods

### Slicing vs list.append/extend

```python
lst = [1, 2, 3]

# Slice assignment
lst[len(lst):] = [4, 5]
print(lst)
# [1, 2, 3, 4, 5]

# Extend (more readable)
lst.extend([6, 7])
print(lst)
# [1, 2, 3, 4, 5, 6, 7]
```

---

### Slicing vs reversed()

```python
lst = [1, 2, 3, 4, 5]

# Slicing (creates new list)
rev1 = lst[::-1]
print(rev1)
# [5, 4, 3, 2, 1]

# reversed() (returns iterator)
rev2 = list(reversed(lst))
print(rev2)
# [5, 4, 3, 2, 1]

# reversed() is more explicit but slicing is more common
```

---

## Performance Considerations

### Time complexity

```python
lst = [1, 2, 3, 4, 5]

# Creating a slice: O(k) where k is slice length
subset = lst[1:4]  # O(3)

# Copying entire list: O(n)
copy = lst[:]  # O(n)

# Slice assignment: O(k + m)
# where k is length of slice, m is length of replacement
lst[1:3] = [10, 11, 12]  # O(2 + 3)
```

---

### Space complexity

```python
# Slicing always creates a new object: O(k) space
lst = list(range(1000000))

subset = lst[:10]  # O(10) space (not O(1000000))

# If you only need to iterate, use itertools.islice
from itertools import islice

for item in islice(lst, 10):
    print(item)
# No extra space for subset
```

---

## Quick Reference Table

| Pattern | Slice | Result |
|---------|-------|--------|
| First 3 | `lst[:3]` | `[0, 1, 2]` |
| Last 3 | `lst[-3:]` | `[7, 8, 9]` |
| All except first | `lst[1:]` | `[1, 2, ..., 9]` |
| All except last | `lst[:-1]` | `[0, 1, ..., 8]` |
| Copy | `lst[:]` | `[0, 1, ..., 9]` |
| Reverse | `lst[::-1]` | `[9, 8, ..., 0]` |
| Every 2nd | `lst[::2]` | `[0, 2, 4, 6, 8]` |
| Middle | `lst[1:-1]` | `[1, 2, ..., 8]` |
| Odd indices | `lst[1::2]` | `[1, 3, 5, 7, 9]` |

---

## Key Takeaway for Interviews

**Golden phrase:**

> "Slicing creates a new sequence in O(k) time where k is the slice length. It's non-destructive and never raises IndexError for out-of-range indices."

**Mental model:**

Think of slicing as defining a window over your sequence. The window's start, end, and stride are controlled by three parameters, all of which are optional.

**When to mention in interviews:**

- "I'll use slicing to create a copy: `lst[:]`"
- "Reversing with `[::-1]` is O(n) time and space"
- "For rotation, I can use slicing: `lst[k:] + lst[:k]`"
- "Slicing doesn't raise errors for out-of-range indices, unlike direct indexing"

---

**Last Updated:** February 7, 2026
