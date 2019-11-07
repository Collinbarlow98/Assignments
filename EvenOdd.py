def ask_user_input():
    greet = "Hello please enter an integer!"
    print(greet)

ask_user_input()

def user_input():
    number = int(input("Integer: "))
    return number

def even_or_odd():
    if (user_input() % 2 == 0):
        print("is an even number.")
        print("------------------")
    else:
        print("is an odd number.")
        print("-----------------")
    return even_or_odd()

even_or_odd()

user_input()
