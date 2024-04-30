#!/usr/bin/env python3

FIRST_LINE_CONST = "SpriteTempVar0 = ActualAddress"
ADD_CONST = "SpriteTempVar0 = SpriteTempVar0 + "
VALUE_CONST = "SpriteTempVar1 = "

def main():
    data = ""
    tuples = []

    with open("function.txt", "r") as f:
        data = f.read()

    lines = data.split("\n")
    for i in range(len(lines)):
        line = lines[i]
        if FIRST_LINE_CONST in line:
            value_line = lines[i+1]
            value = int(value_line.split(VALUE_CONST)[1])
            tuples.append((0, value))
        if ADD_CONST in line:
            increment = int(line.split(ADD_CONST)[1])
            value_line = lines[i+1]
            value = int(value_line.split(VALUE_CONST)[1])
            tuples.append((increment, value))
    
    print("local tuples = {")
    for increment, value in tuples:
        print("    {" + str(increment) + ", " + str(value) + "},")
    print("}")

if "__main__" == __name__:
    main()