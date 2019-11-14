def greeting():
    greet = "Hello please enter an integer!"
    print(greet)

greeting()

number = input("Integer: ")

def odd_even():
    if number.isdigit() == True:
        tnumber = int(number)
        if (tnumber % 2 == 0):
            print("----------------------")
            print(f"|{tnumber} is an even number.|")
            print("----------------------")
        else:
            print("---------------------")
            print(f"|{tnumber} is an odd number.|")
            print("---------------------")
    else:
        print("---------")
        print("|invalid|")
        print("---------")


odd_even()
