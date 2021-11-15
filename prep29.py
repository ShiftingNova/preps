def sum_nums(thing):
    total = 0
    for i in thing:
        temp = list[i]
        for e in i:
            if e < 10:
                total += e
    return total
