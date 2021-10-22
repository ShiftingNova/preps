def most_common_vehicle(file):
    car = open(file, "r")

    high_number = 0
    common_car = ""
    thing = 0
    for i in range(3):
        file_number = file.readline()
        if high_number < file_number:
            thing = i+1
            high_number = file_number
        elif high_number == file_number:
            common_car = "There's a tie!"
    if thing == 1:
        common_car = "Toyota most common"
    elif thing == 2:
        common_car = "Ford most common"
    elif thing == 3:
        common_car = "Chevy most common"
    return (common_car)
