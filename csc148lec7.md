# CSC148 Jan 23 2017

## Recursion

1. Binary :pencil2:

Definition: Binary code is just a string of 0s and 1s.

Ex:

'11100'

'01000011'

''

'0'

'1'

We're going to be given an integer r, and we want to generate all binary codes of length r.

```python

def codes(r):
  if r==0:
    return ['']
  if r > 0:
    smaller = codes(r-1)
    result = [] #this will be all length-r codes
    for code in smaller: #code is a string
      result.append(code + '0')
      result.append(code + '1')
    return result

  '''

  '''

```
