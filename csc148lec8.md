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

1. Suppose we have a single disc to move from peg 1 to peg 3. also peg 2 and peg 3 are empty.
- we have to move this disc without putting it on top of something smaller.
- ... == just move disc from peg 1  to peg 3

Peg 1: 1
Peg 2: |
       V
Peg 3: 1

How do we solve the problem for 0 discs?
do nothing

recursive case: we have more than 1 disc to move from peg 1 to peg 3. 
