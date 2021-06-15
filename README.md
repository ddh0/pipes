# pipes.Pipeline
A tiny, pure-python class for sending and receiving data in a queue.

# Features
- No dependencies other than the Python 3 bultins
- Functional and readable
- Simple to use, with only three methods
- Pipeline objects are ```pickle```-able, and thus easily persistent between sessions or shared however you like

# Examples

FIFO mode - First in, first out:

```
>>> import pipes
>>> P = pipes.Pipeline()
>>> P.add("first")
>>> P.add("second")
>>> P.add("third")
>>> P.get()
'first'
>>> P.get()
'second'
>>> P.get()
'third'
>>>
```

LIFO mode - Last in, first out:

```
>>> import pipes
>>> P = pipes.Pipeline(mode="LIFO")
>>> P.add("first")
>>> P.add("second")
>>> P.add("third")
>>> P.get()
'third'
>>> P.get()
'second'
>>> P.get()
'first'
>>>
```

Pipeline.flush - Reset the pipeline to its original state

```
>>> import pipes
>>> P = pipes.Pipeline()
>>> P.add("junk")
>>> P.add("stuff")
>>> P.add("things")
>>> P.flush()
>>> P.get()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Dylan\PY3\pipes\pipes.py", line 54, in get
    raise IndexError("Empty Pipeline")
IndexError: Empty Pipeline
>>>
```

# That's it?
Yep! This module was designed for this purpose and this purpose only, and it does its job very well.
