import sys

from stats import count_words, count_characters, convert_to_sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
def format_characters(list_of_characters):
    for i in list_of_characters:
        if i["name"].isalpha():
            print(f"{i["name"]}: {i["value"]}")

def verify_input():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def main():
    verify_input()

    book_path = sys.argv[1]
    book = get_book_text(book_path)
    words_in_book = count_words(book)
    characters_in_book = count_characters(book)
    sorted_list = convert_to_sorted_list(characters_in_book)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_in_book} total words")
    print("--------- Character Count -------")
    format_characters(sorted_list)
    print("============= END ===============")


main()