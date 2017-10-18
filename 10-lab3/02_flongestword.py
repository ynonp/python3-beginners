# A function to return the longest word in a sentence
def longest_word(sentence):
    # This code is taken from a previous solution we saw
    # only this time sentence is read from the calling code
    result = ""
    for word in sentence.split():
        if len(word) > len(result):
            result = word

    # and result is "returned" and not printed    
    return result
            
word = longest_word("hello mr joe")
# this will hopefully print hello
print(word)
