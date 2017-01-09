# CSC148 Jan 9 2017

## Abstract Data Types (ADTs)

- Abstraction: ignoring certain details to make problems easier to solve
- _Abstract_ because there is no mention of implementation details
- _Data Type_ because it includes data and operations on those
- Allows us to directly describe the data used in our problems, independent of implementation details
- In fact, you've worked with some ADTS (dictionaries)

## Stack ADT

- A stack is a sequence of objects
- Objects are removed in the opposite order that they are inserted
- Last in, first out (LIFO), like putting away and taking out plates
- The object last inserted is at the __top__ of the stack

```python
#Stack principle: things are removed in the opposite order that they are inserted
def second(value):
  result = abs(value)
  return result

def first(value):
  result = second(value)
  return "value = " + str(value)

def main():
  value = -50
  result = first(value)
  print(result)
  return None

main()

#main gets called ->
#first gets called ->
#second gets called ->
#second returns ->
#first returns ->
#main returns
```

We'll use this real-world description of a stack for our design:

> A stack contains items of various sorts. New items are pushed onto the top of the stack, items may only be popped from the top of the stack. It's a mistake to try to remove an item from an empty stack. We can tell how big a stick is, and what the top item is.

## Stack operations

- push(o) Add a new item o to the top of the stack
- pop() remove and return top item
- is_empty() Test if stack is empty:

Could also add:
- peek()

```python
from Stack import Stack

s1 = Stack()
s1.push(4)
s1.push(6)
s1.pop()
#o
s1.pop()
#4
s1.pop()
#Error
```

## implementation possibilities
- The public interface of our Stack ADT should be constant, but inside we could implement it in various ways

## Stack Example
- Start with empty stack [ ]
- push 5: [5]
- push 8: [5, 8]
- Pop: [5] (and returns 8)
- Pop: [] (and returns 5)
- Pop: error!
