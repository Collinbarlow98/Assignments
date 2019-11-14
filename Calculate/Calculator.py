def calculate():
    first_number = int(input("First Number: "))
    operand = input("Operand: ")
    second_number = int(input("Second Number: "))

    if operand == "+":
        print(first_number + second_number)
    elif operand == "-":
        print(first_number - second_number)
    elif operand == "*":
        print(first_number * second_number)
    elif operand == "/":
        print(first_number / second_number)
    else:
        print("Incorrect input")
    return calculate()

calculate()

#def ask_user_for_input():
#    first_number = int(input("First Number: "))
#    operand = input("Operand: ")
#    second_number = int(input("Second Number: "))
#    return(first_number, operand, second_number)
#
#def add(a,b):
#    return a+b
#
#def subtract(a,b):
#    return a-b
#
#def display_result(a, b, op, result):
#    print(f"{a} {op} {b} = {result})
#
#(no1, op, no2) = ask_user_for_input()
#
#if operand == "+":
#        print(first_number + second_number)
#elif operand == "-":
#        print(first_number - second_number)
#elif operand == "*":
#        print(first_number * second_number)
#elif operand == "/":
#        print(first_number / second_number)
