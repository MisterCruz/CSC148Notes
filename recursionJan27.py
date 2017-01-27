def codes(r):
    '''(int)->list of str

    Return all binary codes of length r
    '''
    if r == 0:
        return ['']
    small = codes(r-1)
    lst = []
    for item in small:
        lst.append('0' + item)
        lst.append('1' + item)
    return lst

print(codes(2))
