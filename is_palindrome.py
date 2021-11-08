word = input('enter the object: ')
list = []
list.append(word.upper())

for elem in list:
    if elem[::-1] == elem: print(word)
    else: print('it is not a palindrome')