**Precondition:**

```python
len(set(map(abs, array))) == len(set(array))
0 <; len(array) < 100
all(isinstance(x, int) for x in array)
all(-100 < x < 100 for x in array)
```