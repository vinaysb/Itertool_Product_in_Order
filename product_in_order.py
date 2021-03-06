def product_in_order(*args, repeat=1):
    '''
    It accepts 1 iterable and returns a product of the iterable with itself but in order, for example,
    product(['A', 'B', 'C', 'D'], repeat=2) --> ('A', 'B') ('B', 'C') ('C', 'D')
    product(list(range(10)), repeat=3) --> (0, 1, 2) (1, 2, 3) (2, 3, 4) (3, 4, 5) (4, 5, 6) (5, 6, 7) (6, 7, 8) (7, 8, 9)
    '''
    pools = [list(pool) for pool in args][0]
    result = []
    for i, x in enumerate(pools):
        temp = []
        for y in pools[i + 1:i + repeat]:
            temp.append(y)
        if len(temp) == repeat - 1:
            result.append([])
            result[i].append(x)
            result[i].extend(temp)
    for prod in result:
        yield tuple(prod)
