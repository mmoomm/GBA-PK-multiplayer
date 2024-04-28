#!/usr/bin/env python3

#VALUE_CONST = "ScriptAddressTemp1 ="
VALUE_CONST = "SpriteTempVar1 ="
def main():
    data = ""
    values = []

    with open("function.txt", "r") as f:
        data = f.read()

    data = data.split("\n")
    for line in data:
        if VALUE_CONST in line:
            values.append(line.split(VALUE_CONST)[1])
    
    print("local values = {" + ", ".join(str(num) for num in values) + "}")
    print("main")

if "__main__" == __name__:
    main()
