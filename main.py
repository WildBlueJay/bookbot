def main():
    book_path = "books/frankenstein.txt"  
    file_contents = get_book_text(book_path)
    print(file_contents)
    num_words = word_count(file_contents)
    print(f"{num_words} word[s] found in the text")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(source):
    words = source.split()
    return len(words)

def character_count(source):
    #Count characters using dictionary. Use .lower() method to convert to lowercase
    return None #TEMP

main()    