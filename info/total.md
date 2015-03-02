Some joker has written minuses on our troopers' numbers and now the ordering program is broken.
We should update the sorting algorithm.

Let's try some sorting. Here is an array with specific rules.

The array has various numbers. You should sort it, but sort it by absolute value in ascending order.
For example, the sequence (-20, -5, 10, 15) will be sorted like so: (-5, 10, 15, -20).
Your function should return the sorted list or tuple.

**Input:** An array of numbers a tuple.

**Output:** The list or tuple (but not a generator) sorted by absolute values in ascending order.

**Example:**

```python
absolute_sorting((-20, -5, 10, 15)) == [-5, 10, 15, -20] # or (-5, 10, 15, -20)
absolute_sorting((1, 2, 3, 0)) == [0, 1, 2, 3]
absolute_sorting((-1, -2, -3, 0)) == [0, -1, -2, -3]
```
**How it is used:**

Sorting is a part of many tasks, so it will be useful to know how to use it.

**Precondition:**

```python
len(set(map(abs, array))) == len(set(array))
0 <; len(array) < 100
all(isinstance(x, int) for x in array)
all(-100 < x < 100 for x in array)
```
