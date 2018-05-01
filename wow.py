from functools import reduce

#print reduce((lambda x, y: x + 1), [1,2,3])


f = open("book.txt", "r")
book = f.read()
words = book.split()

#print words
z = 0


def word_freq(book, word):
    freq = [1 for x in book if x.lower() == word]
    if len(freq) == 0:
        freq = [0,0]
    return reduce((lambda x,y: x + y), freq)


def group_freq(book, word_list):
    freq = [word_freq(book,x) for x in word_list]
    return reduce((lambda x,y: x + y), freq)

def most_freq(book):
    freq = [(x,word_freq(book, x)) for x in book]
    return max(freq)[0]
    

print("frequency of 'the' in the book:")
print word_freq(words, "the")
print("frequency of 'dog' in the book:")
print word_freq(words, "dog")
print("frequency of 'the' and 'dog' in the book:")
print group_freq(words, ["the", "dog"])
print("most frequent word:")
print most_freq(words)
