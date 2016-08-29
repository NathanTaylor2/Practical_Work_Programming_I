
word_count = dict()
text = input("Text: ").lower().split()

for word in text:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
for word in word_count:
    print(word, ": ", word_count[word])

#TODO Format the print properly