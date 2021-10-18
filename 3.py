sentence = input('enter sentence : ')
words = 0
for char in sentence:
    if char == ' ':
        words +=1

print('number of words : {}'.format(words))