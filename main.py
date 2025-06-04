import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path_to_book = sys.argv[1]


def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
        return contents 

from stats import word_count
from stats import char_count
from stats import sort

def main():
    #book_contents = get_book_text("./books/frankenstein.txt")
    book_contents = get_book_text(path_to_book)
    counting = word_count(book_contents)
    character_count = char_count(book_contents)
    report = sort(character_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print (f"Found {counting} total words")
    print("--------- Character Count -------")

    for item in report:
        if item["char"].isalpha():
           item_letter = item["char"]
           item_count =  item["num"]
           print(f"{item_letter}: {item_count}")
    print("============= END ===============")

main()
