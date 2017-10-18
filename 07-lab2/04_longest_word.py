# First let's ask the user for a sentence
sentence = input("Type in a sentence: ")

# Now comes the fun part.
# Just like when we calculated the sum, we need a variable
# to hold the longest word
longest_word = ""

# A for loop can iterate each word using split
for word in sentence.split():
    # But instead of adding new words to that accumulator
    # variable we defined (longest_word), we should
    # change its value when we find words that are longer
    # than the current one
    if len(word) > len(longest_word):
        longest_word = word

# Now we have the longest word in longest_word variable
# and we're ready to print it and impress our user
print("The longest word is:",longest_word)
