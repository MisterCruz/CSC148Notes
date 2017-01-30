# CSC148 Lecture 8 January 30

## Towers of Hanoi
- you have three pegs, and a bunch of discs
- all discs start off on peg 1
- they're stacked so that the largest disc is on the bottom, second-largest is on top of that, third-largest on top of that...
- goal: move all discs from the first peg to the third peg
- you can only move one disc at a time
- you can never put a bigger disc on top of a smaller disc
- First peg is where the discs start, third peg is where they end up, and second peg is for temporary storage

Suppose that we have three discs on peg 1.
Peg 1: 3 2 1
It will take 7 moves to solve this puzzle.

recursive formulation of how to solve this problem:

###  Suppose we have a single disc to move from peg 1 to peg 3. also peg 2 and peg 3 are empty.
- we have to move this disc without putting it on top of something smaller.
- ... == just move disc from peg 1  to peg 3

Peg 1: 1
Peg 2: |
       V
Peg 3: 1

How do we solve the problem for 0 discs?
do nothing

recursive case: we have more than 1 disc to move from peg 1 to peg 3.

Let _n_ be the number of discs to move from peg 1 to peg 3

we have to think of a smaller subproblem with exactly the same structure

1. here's a subproblem: move n-1 discs from peg 1 to peg2.
this moves everything off peg1 except the bottom disc.

peg1: 5 4 3 2 1
peg2:
peg3:

...

peg1: 5
peg2: 4 3 2 1
peg3:

...

peg1:
peg2: 4 3 2 1
peg3: 5

...

peg1:
peg2:
peg3: 5 4 3 2 1

2. move that biggest disc from peg1 to peg3
3. move the n-1 discs from peg2 to peg3

```python
def hanoi(n, peg1, peg2, peg3):
  #peg1 is starting point
  #peg2 is temp storage
  #peg3 is destination
  #n discs to move
  if n == 1:
    print('Move from', peg1, 'to', peg3)
    return
  hanoi(n-1, peg1, peg3, peg2)
  print('Move from', peg1, 'to', peg3)
  hanoi(n-1, peg2, peg1, peg3)
```

  ```python
  def rec_max(lst):
    '''return max number in possibly nested list of numbers.

    >>> rec_max([17, 21, 0])
    21
    >>> rec_max([17, [21, 24], 0])
    24
    '''
    nums = []
    for element in lst:
      if isinstance(element, int):
        nums.append(element)
      else:
        nums.append(rec_max(element))
    return max(nums)

    ```

    rec_max([4, [5, 6], [7, [8, 9]]])

    what does rec_max return on [5, 6]
    >>> rec_max([5, 6])
    6

    >>> rec_max([8, 9])
    9

    >>> rec_max([7, [8, 9]])
    nums = []
    7... nums =[7]
    [8, 9]...   
    wdq
