## I have no idea how to start solving this mission
First, read about [sorted](http://docs.python.org/2/library/functions.html#sorted) and
[abs](http://docs.python.org/2/library/functions.html#abs).
```python
abs(5) == abs(-5) == 5
sorted([1, 5, 2, -3]) == [-3, 1, 2, 5]
```

## I need some help to proceed with the mission

You should try to use [the key parameter for sorting](https://wiki.python.org/moin/HowTo/Sorting/#Key_Functions).

```python
#sort by last digit for numbers from 10 to 99 only
sorted([11, 20, 54, 73], key=lambda x: str(x)[1]) == [20, 11, 73, 54]
#sort lists by sums
sorted([[90, 11], [99, 1], [200], [30, 50, 50]], key=sum) == [[99, 1], [90, 11], [30, 50, 50], [200]]
```

"key" doesn't change elements.

## I am gone half way through. Need help!

Look carefully at the last hint and first hint, then place your "key".
