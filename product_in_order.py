def product_in_order(*args, repeat=1):
    # product(['A', 'B', 'C', 'D'], repeat=2) --> ('A', 'B') ('B', 'C') ('C', 'D')
    # product(list(range(10)), repeat=3) --> 012 123 234 345 456 567 678 789
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
