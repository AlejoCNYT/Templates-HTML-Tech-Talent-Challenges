letter = 'prontosaurio'

dictionary = dict()
for character in letter:
    dictionary[character] = dictionary.get(character, 0) + 1
print(dictionary)
