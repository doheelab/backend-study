## Iterables

- lists, strings are _iterable_.

* These **iterables** are handy because you can read them as much as you wish, but **you store all the values in memory** and this is not always what you want when you have a lot of values.

## Generators

Generators are iterators, a kind of iterable **you can only iterate over once**. Generators do not store all the values in memory, they **generate the values on the fly**.

```python
>>> mygenerator = (x*x for x in range(3))
>>> for i in mygenerator:
...    print(i)
```

It is just the same except you used `()` instead of `[]`. BUT, you cannot perform `for i in mygenerator` a second time since generators can only be used once: they calculate 0, then forget about it and calculate 1, and end calculating 4, one by one.

## Yield

`yield` is a keyword that is used like `return`, except the function will return a generator.

```python
>>> def createGenerator():
...    mylist = range(3)
...    for i in mylist:
...        yield i*i
...
>>> mygenerator = createGenerator() # create a generator
>>> print(mygenerator) # mygenerator is an object!
<generator object createGenerator at 0xb7555c34>
>>> for i in mygenerator:
...     print(i)
0
1
4
```

Here it's a useless example, but it's handy when you know your function will return a huge set of values that you will only need to read once.

> 함수를 호출해도 함수 내에 있는 코드들이 실행되지 않는다.

To master `yield`, you must understand that **when you call the function, the code you have written in the function body does not run.** The function only returns the generator object, this is a bit tricky :-)

Then, your code will continue from where it left off each time `for` uses the generator.

> 코드는 실제로 for 루프로 제너레이터를 돌 때 실행됩니다.

The first time the `for` calls the generator object created from your function, it will run the code in your function from the beginning until it hits `yield`, then it'll return the first value of the loop. Then, each subsequent call will run another iteration of the loop you have written in the function and return the next value.

> 더 이상 yield를 만나지 못했을 때 다 끝난 것으로 간주합니다.

This will continue until the generator is considered empty, which happens when the function runs without hitting `yield`. That can be because the loop has come to an end, or because you no longer satisfy an `"if/else"`.

---

## Generator

```python
>>> class Bank(): # Let's create a bank, building ATMs
...    crisis = False
...    def create_atm(self):
...        while not self.crisis:
...            yield "$100"
>>> hsbc = Bank() # When everything's ok the ATM gives you as much as you want
>>> corner_street_atm = hsbc.create_atm()
>>> print(corner_street_atm.next())
$100
>>> print(corner_street_atm.next())
$100
>>> print([corner_street_atm.next() for cash in range(5)])
['$100', '$100', '$100', '$100', '$100']
>>> hsbc.crisis = True # Crisis is coming, no more money!
>>> print(corner_street_atm.next())
<type 'exceptions.StopIteration'>
>>> wall_street_atm = hsbc.create_atm() # It's even true for new ATMs
>>> print(wall_street_atm.next())
<type 'exceptions.StopIteration'>
>>> hsbc.crisis = False # The trouble is, even post-crisis the ATM remains empty
>>> print(corner_street_atm.next())
<type 'exceptions.StopIteration'>
>>> brand_new_atm = hsbc.create_atm() # Build a new one to get back in business
>>> for cash in brand_new_atm:
...    print cash
$100
$100
$100
$100
$100
$100
$100
$100
$100
...
```

## Caller

```python

# Create an empty list and a list with the current object reference
result, candidates = list(), [self]

# Loop on candidates (they contain only one element at the beginning)
while candidates:

    # Get the last candidate and remove it from the list
    node = candidates.pop()

    # Get the distance between obj and the candidate
    distance = node._get_dist(obj)

    # If distance is ok, then you can fill the result
    if distance <= max_dist and distance >= min_dist:
        result.extend(node._values)

    # Add the children of the candidate in the candidate's list
    # so the loop will keep running until it will have looked
    # at all the children of the children of the children, etc. of the candidate
    candidates.extend(node._get_child_candidates(distance, min_dist, max_dist))

return result

```

# Reference

[What does the “yield” keyword do?] https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do/231855#231855

[번역] https://tech.ssut.me/what-does-the-yield-keyword-do-in-python/
