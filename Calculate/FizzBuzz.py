fizz = "Fizz"
buzz = "Buzz"
no_fizz_buzz = "Where is FizzBuzz?"

def ask_user_input():
    greet = "Hello please enter an integer!"
    print(greet)

def fizz_buzz():
    number = int(input("Number: "))
    if (number % 3 == 0 and number % 5 == 0):
        print(fizz + buzz)
    elif (number % 5 == 0):
        print(buzz)
    elif (number % 3 == 0):
        print(fizz)
    else:
        print(no_fizz_buzz)
    return fizz_buzz()

fizz_buzz()
