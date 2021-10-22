def grade_info(list):
    max = 0
    min = 100000000000000
    average = 0
    for i in range(len(list)):
        average += list[i]
        if max <list[i]:
            max = list[i]
        if min > list[i]:
            min = list[i]
    return(max,min,(average/len(list)))
