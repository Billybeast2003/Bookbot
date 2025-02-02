path_to_file = 'books/frankenstein.txt'

def get_data(path_to_file):
    with open(path_to_file, 'r') as file:
        text = file.read()
    return text


def get_num_words(text):
    words = text.split()
    return len(words)

# Add a new function to your script that takes the text from the book as a string, and returns the number of times each character, including symbols and spaces, appears in the string. Convert any character to lowercase, we don't want duplicates.

def get_char_count(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def report(path_to_file):
    text = get_data(path_to_file)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    print(f'--- Begin report of {path_to_file} ---')
    print(f"{num_words} words found in the document.")
    # get only the characters
    char_count = {k: v for k, v in char_count.items() if k.isalpha()}
    for char, count in char_count.items():
        print(f"The {char} was found {count} times")
        
    print(f'--- End report ---')
    
report(path_to_file)
