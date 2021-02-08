## 이터레이터란?

이터레이터(iterator)는 값을 차례대로 꺼낼 수 있는 객체(object)입니다.

메모리를 효율적으로 사용하기 위해서, 파이썬에서는 이터레이터만 생성하고 값이 필요한 시점이 되었을 때 값을 만드는 방식을 사용합니다.

## Iterable

반복 가능한 객체는 말 그대로 반복할 수 있는 객체인데 우리가 흔히 사용하는 문자열, 리스트, 딕셔너리, 세트가 반복 가능한 객체입니다. 즉, 요소가 여러 개 들어있고, 한 번에 하나씩 꺼낼 수 있는 객체입니다.

```python
>>> dir([1, 2, 3])
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

리스트 [1, 2, 3]을 dir로 살펴보면 **iter** 메서드가 들어있습니다. 이 리스트에서 **iter**를 호출해보면 이터레이터가 나옵니다.

```python
>>> [1, 2, 3].__iter__()
<list_iterator object at 0x03616630>
```

리스트의 이터레이터를 변수에 저장한 뒤 **next** 메서드를 호출해보면 요소를 차례대로 꺼낼 수 있습니다.

```python
>>> it = [1, 2, 3].__iter__()
>>> it.__next__()
1
>>> it.__next__()
2
>>> it.__next__()
3
>>> it.__next__()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    it.__next__()
StopIteration
```

it에서 **next**를 호출할 때마다 리스트에 들어있는 1, 2, 3이 나옵니다. 그리고 3 다음에 **next**를 호출하면 StopIteration 예외가 발생합니다. 즉, [1, 2, 3]이므로 1, 2, 3 세 번 반복합니다.

## 이터레이터 만들기

```python
class Counter:
    def __init__(self, stop):
        self.current = 0    # 현재 숫자 유지, 0부터 지정된 숫자 직전까지 반복
        self.stop = stop    # 반복을 끝낼 숫자

    def __iter__(self):
        return self         # 현재 인스턴스를 반환

    def __next__(self):
        if self.current < self.stop:    # 현재 숫자가 반복을 끝낼 숫자보다 작을 때
            r = self.current            # 반환할 숫자를 변수에 저장
            self.current += 1           # 현재 숫자를 1 증가시킴
            return r                    # 숫자를 반환
        else:                           # 현재 숫자가 반복을 끝낼 숫자보다 크거나 같을 때
            raise StopIteration         # 예외 발생

for i in Counter(3):
    print(i, end=' ')

>>> 0 1 2
```

## 인덱스로 접근 가능한 이터레이터

앞에서 만든 Counter 이터레이터를 인덱스로 접근할 수 있도록 다시 만들어보겠습니다.

```python
class Counter:
    def __init__(self, stop):
        self.stop = stop

    def __getitem__(self, index):
        if index < self.stop:
            return index
        else:
            raise IndexError

print(Counter(3)[0], Counter(3)[1], Counter(3)[2])

for i in Counter(3):
    print(i, end=' ')

>>> 0 1 2
>>> 0 1 2

```

## iter, next 함수 활용하기

iter는 반복 가능한 객체에서 이터레이터를 반환하고, next는 이터레이터에서 값을 차례대로 꺼냅니다.

```python
>>> it = iter(range(3))
>>> next(it)
0
>>> next(it)
1
>>> next(it)
2
>>> next(it)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    next(it)
StopIteration
```

## dir

객체의 메서드를 확인하는 방법

## Reference

https://dojang.io/mod/page/view.php?id=2405

https://dojang.io/mod/page/view.php?id=2406

https://dojang.io/mod/page/view.php?id=2407

https://dojang.io/mod/page/view.php?id=2408
