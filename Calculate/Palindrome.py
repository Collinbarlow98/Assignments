word = input("Enter a word: ").lower()
reversed_word = ""

for index in range(len(word)-1,-1,-1):
    reversed_word += word[index]

if word == reversed_word:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
