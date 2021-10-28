def every_other(word):
    word = word.split(" ")
    line =""
    i=0
    while i <len(word):
        if i %2==0:
            line = line+word[i] +" "
        i +=1
    return line
