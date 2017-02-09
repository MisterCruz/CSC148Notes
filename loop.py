def dot_prod(u: [float, ...], v: [float, ...]) -> float:
    """Return the dot product of u and v

    u, v --- non-empty lists of the same length

    >>> dot_prod([1.0, 2.0], [3.0, 4.0])
    11.0

    [1.0, 2.0] * [3.0, 4.0] = (1 * 3) + (2 * 4) = 11
    """
    # sum of products of pairs of corresponding coordinates of u and v
    total = 0
    for i in range(len(u)):
        total += u[i] * v[i]

    return total

#List Comprehension version
def dot_prodComp(u: [float, ...], v: [float, ...]) -> float:
    """Return the dot product of u and v

    u, v --- non-empty lists of the same length

    >>> dot_prod([1.0, 2.0], [3.0, 4.0])
    11.0
    """
    # sum of products of pairs of corresponding coordinates of u and v 
    return sum([u_coord * v_coord for u_coord, v_coord in zip(u, v)])
