letter = 'prontosaurio'
dictionary = dict()

for character in letter:
    if character not in dictionary:
        dictionary[character] = 1
    else:
        dictionary[character] += 1

print(dictionary)
