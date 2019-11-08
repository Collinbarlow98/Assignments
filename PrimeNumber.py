number = int(input("Enter number: "))
prime = number - 1

while prime > 1:
  if (number % prime == 0):
    print("Not Prime")
    break
  elif (number % prime != 0):
    prime += -1

if prime == 1:
  print("Prime")
