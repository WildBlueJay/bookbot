def main():
    book_path = "books/frankenstein.txt"  
    #Retrieve source book
    file_contents = get_book_text(book_path)
    #TEMP print(file_contents)
    #Count and Print word count
    num_words = word_count(file_contents)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} word[s] found in the text")
    #Run and print character counts
    char_counts = character_count(file_contents)
    character_count_print(char_counts)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(source):
    words = source.split()
    return len(words)

def character_count(source):
    lower_case_string = source.lower()
    count_dict = {}
    for char in lower_case_string:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict

def sort_on(dict):
    return dict["num"]

def character_count_print(char_dictionary):
    char_list = []
    # Transform dictionary items into list elements
    for char, count in char_dictionary.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})
    #Alternative, streamlined method
    #  char_list = [{"char": char, "num": count} for char, count in char_dictionary.items() if char.isalpha()]
    char_list.sort(reverse=True, key=sort_on)
    for item in char_list:
        print(f"The '{item['char']}' character was found {item['num']} times.")
    print("---End of Report ---")
    return None

main()    