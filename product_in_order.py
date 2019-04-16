def product_in_order(*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [list(pool) for pool in args][0]
    print(pools)
    result = []
    for i, x in enumerate(pools):
        temp = []
        for y in pools[i + 1:i + repeat]:
            print(y)
            temp.append(y)
        if len(temp) == repeat - 1:
            result.append([])
            result[i].append(x)
            result[i].extend(temp)
    for prod in result:
        yield tuple(prod)
