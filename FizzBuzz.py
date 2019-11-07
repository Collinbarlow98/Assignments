fizz = "Fizz"
buzz = "Buzz"
no_fizz_buzz = "Where is FizzBuzz?"

def fizz_buzz():
    greet = "Hello please enter an integer!"
    print(greet)
    number = int(input("Number: "))
    if (number % 3 == 0 and number % 5 == 0):
        print(fizz + buzz)
    elif (number % 5 == 0):
        print(buzz)
    elif (number % 3 == 0):
        print(fizz)
    else:
        print(no_fizz_buzz)

fizz_buzz()
