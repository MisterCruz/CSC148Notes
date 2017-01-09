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

## Uses for a stack
- Keep track of pages visited in a browswer tab
- keep track of function calls in a running program
- check for balanced parentheses
- keep undo/redo history in a text editor or word processor
- and lots more!

## Queue ADT
- a sequence of objects again, but the operators are different than the stack ones
- objects are removed in the same order they are inserted (first in first out) FIFO

- Example in real life:
  - Lineup at Fresh restaurant
  - First, Michael shows up
  - Then, Nikki shows up
  - Then, dan shows up
  - Then, restaurant opens... who gets in first?
    - Michael
    - Nikki
    - Dan


- enqueue(o) Add o to the end of the Queue
- dequeue() remove and return object at the front of the Queue
- front() return object at the front of the Queue
- is_empty() test if queue is empty
- size() return number of items in Queue

One way to implement a queue:

```python
def enqueue(self, item):
  ... append to right end of a list

def dequeue(self):
  ... remove from the left of the list


```
What does this code do?

Imagine that we have stack s1 with some items in it.
let's say that the items are 3 4 5 6 7 <-- top
7 is top of stack

I want to remove and print every item on the stack
```python
while not s1.is_empty():
  item = s1.pop()
  print(item)
  # or print(s1.pop())

Output:
7 6 5 4 3
```

Let's say that you wanted to print them in the opposite order... how??

```python
lst = []
while not s1.is_empty():
  lst.append(s1.pop())

lst.reverse()
for item in lst:
  print(item)

```
