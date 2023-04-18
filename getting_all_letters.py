import string


with open("letters.txt",'w') as file:
    for letter in string.ascii_lowercase:
        print(letter)
