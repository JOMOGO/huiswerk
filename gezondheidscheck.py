"""
Name:           Robin Groot
Version:        1.0
Inputs:         Heartbeat, Temperature, Pressure
Outputs:        If you are sick or not?
Description:    Tells you if you are sick or not based on your inputs?
"""
# Initialising variables
min_heart = 55
max_heart = 90
min_temp = 36.3
max_temp = 37.5
min_pressure = 100
max_pressure = 140
list_bool = []


def between():
    # Asking for your
    heart = int(input("What is your heartbeat?"))
    temp = int(input("What is your temperature?"))
    pressure = int(input("What is your pressure?"))

    # Make lists containing the inputs and initialised variables
    cal_heart = [min_heart, heart, max_heart]
    cal_temp = [min_temp, temp, max_temp]
    cal_pressure = [min_pressure, pressure, max_pressure]
    cal_list = [cal_heart, cal_temp, cal_pressure]

    # Makes list with True or false
    for item in cal_list:
        if item[0] <= item[1] <= item[2]:
            list_bool.append(False)
        else:
            list_bool.append(True)

    # Tells you if you are sick or not based on True or False
    if list_bool[0] == False and list_bool[1] == False and list_bool[2] == False:
        print("You are not sick")
    else:
        print("You are sick")


# Calls the function that tells you if you are sick based on your input.
between()
