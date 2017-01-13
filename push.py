'''
def push(list):
    pos = 0
    for number in list:
        if number == 0:
            list[-1] = number
        elif number != 0:
            list[pos] = number
            pos += 1
    return list
'''

#print(push([1, 2, 3, 0]))

def push(list):
    pos = 0
    for number in list:
        if number != 0:
            list[pos] = number
            pos = pos + 1
        elif number == 0:
            list.pop(0)
            list[-1] = number
            
    return list

print(push([1, 0, 2]))
