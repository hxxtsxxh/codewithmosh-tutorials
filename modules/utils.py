def find_max(list):
    maximum = list[0]
    for number in list:
        if number > max:
            maximum = number
    return(maximum)
