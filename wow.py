# Charles Weng Dasha Shifrina
# SoftDev2   pd7
# K #18: Reductio ad Absurdum
# 2018-4-30

################################################################################
#                                Initializtion                                 #
################################################################################

from functools import reduce

f = open("book.txt", "r")
book = f.read()
words = book.split()


################################################################################
#                                   Functions                                  #
################################################################################

def word_freq(book, word):
    freq = [1 if x.lower() == word else 0 for x in book]
    return reduce((lambda x, y: x + y), freq)


def group_freq(book, word_list):
    freq = [word_freq(book, x) for x in word_list]
    return reduce((lambda x, y: x + y), freq)

def phrase_freq(book, phrase):
    phrase_split = phrase.split()
    #freq = [1 for x in len(book) if phrase_split == book[x: x + len(phrase_split) ]]
    #return reduce((lambda x,y: x+y,freq))


# direct bash approach; not sure how to optimize
# def most_freq(book):
#     freq = [(x, word_freq(book, x)) for x in book]
#     return max(freq)[0]

# new faster way, but it doesn't use reduce/list comprehension
def most_freq(book):
    temp = {}
    for x in book:
        if x in temp:
            temp[x] = temp[x] + 1
        else:
            temp[x] = 1
    return temp[max(temp)]


################################################################################
#                                   Testing                                    #
################################################################################

print "hi"
print("frequency of 'the' in the book:")
print word_freq(words, "the")
print("frequency of 'dog' in the book:")
print word_freq(words, "dog")
print("frequency of 'the' and 'dog' in the book:")
print group_freq(words, ["the", "dog"])
print("frequency of 'in the' in the book:")
print phrase_freq(words, "in the")

# most_freq takes a very long time to process

print("most frequent word:")
print most_freq(words)
