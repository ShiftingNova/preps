def differences(set1,set2):
    total = 0
    for i in set1:
        if i not in set2:
            total += 1
    for i in set2:
        if i not in set1:
            total += 1
    return total
