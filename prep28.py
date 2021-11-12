def get_elements(dic,num):
    list = []
    for key in dic:
        length = len(key)
        value = dic.get(key)
        if key[0]==key[0].upper():
            list.append(value)
        elif key[length-1] == key[length-1].upper():
            list.append(value)
        elif value < num:
            list.append(value)
    return list
