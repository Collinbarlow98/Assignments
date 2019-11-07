def even_or_odd():
    greet = "Hello please enter an integer!"
    print(greet)
    number = int(input("Integer: "))
    return number

if (even_or_odd() % 2 == 0):
    print("That number is even.")
else:
    print("That number is odd.")
