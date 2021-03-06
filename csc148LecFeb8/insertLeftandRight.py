def binary_tree(value):
    return [value, None, None]

def insert_left(bt, value):
    '''Insert value as the left node of the root of bt.'''
    if not bt:
        raise ValueError('cannot insert into empty tree')
    left_branch = bt.pop(1)
    bt.insert(1, [value, left_branch, None])

def insert_right(bt, value):
    if not bt:
        raise ValueError('cannot insert into empty tree')

    right_branch = bt.pop(2)
    bt.append([value, None, right_branch])
    # we are inserting into the right subtree
    # and making the old right subtree be the right subtree
    # of the new right subtree

def contains(bt, value):
    '''(BT, value) -> bool
    Return True iff value is in bt.

    >>> contains([4, [5, None, None], None], 5)
    True

    '''
    if not bt:
        return False

    # found at root, or in left, or in right
    
    return bt[0] == value or contains(bt[1], value) or contains(bt[2], value)

    
