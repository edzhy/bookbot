def main():
    path_to_book = "books/frankenstein.txt"
    book_text = file_to_text(path_to_book)
    num_words = word_count(book_text)
    letter_dict = letter_management(book_text)

    letters = dict_to_list(letter_dict)
    letters.sort(reverse = True, key = sort_on)
    reporting(path_to_book,letters,num_words)
    
#builds a visually appealing print statement to see stats of the book
def reporting(path_to_file, list, num):
    print(f"--- Begin report of {path_to_file} ---")
    print(f"The book contains {num} words\n")
    for dictionary in list:
        print(f"The '{dictionary['char']}' character was found {dictionary['count']} times")
    print("--- End report ---")


#this function creates a list of dictionaries out of letter_dict
#and sorts it descending
def dict_to_list(dict):
    list_of_dicts = []
    for key, value in dict.items():
        list_of_dicts.append({"char":key, "count":value})
    return(list_of_dicts)
def sort_on(dict):
    return dict["count"]

#takes a string as parameter, 
#and returns count of words in the string
def word_count(text):
    words = text.split()
    return len(words)

#takes a string as param,
#returns a dictionary where lower case letter is key
#and value represents how many times in string the letter repeats
def letter_management(text):
    char_dict = {}
    words = text.lower().split()
    for word in words:
        for character in word:
            if character.isalpha():
                if character in char_dict:
                    char_dict[character] += 1
                else:
                    char_dict[character] = 1
    return char_dict

#takes a path to file as param, 
#and within the wrapper accesses file contents
#returns a string
def file_to_text(path):
    with open(path) as f:
        return f.read() #returns a string containing the whole book

if __name__ == "__main__":
    main()
