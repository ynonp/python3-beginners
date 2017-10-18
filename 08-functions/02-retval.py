def count_words(sentence):
    return len(sentence.split())

wc = count_words("baby let me follow you down")
print("sentence has %d words" % wc)

s = "baby let me follow you down"
t = "I have a dream"

if count_words(s) > count_words(t):
    print("s has more words")
else:
    print("t has more words")


