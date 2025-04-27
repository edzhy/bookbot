#takes a string as parameter, 
#and returns count of words in the string
def word_count(text):
    words = text.split()
    return len(words)