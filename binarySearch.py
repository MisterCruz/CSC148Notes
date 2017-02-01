'''
Binary Search vs. Linear Search

- Another example of recursion

How do you search a list?
'''
#Linear Search
def search_list(lst, value):
    for element in lst:
        if element == value:
            return True
    return False

#Binary Search

def binary_search(lst, value):
    lower = 0
    upper = len(lst)
    while lower < upper:
        x = lower + (upper - lower) // 2
        val = lst[x]
        if value == val:
            return x
        elif value > val:
            if lower == x:
                break
            lower = x
        elif value < val:
            upper = x

