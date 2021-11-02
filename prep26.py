def differences(set1,set2):
    total = 0
    for i in set1:
        if i not in set2:
            total += 1
    return total
