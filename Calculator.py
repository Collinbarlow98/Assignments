first_number = int(input("First Number: "))
operand = input("Operand: ")
second_number = int(input("Second Number: "))
if operand == "+":
    sum = first_number + second_number
    print(sum)
if operand == "-":
    difference = first_number - second_number
    print(difference)
if operand == "*":
    product = first_number * second_number
    print(product)
if operand == "/":
    quotient = first_number / second_number
    print(quotient)
