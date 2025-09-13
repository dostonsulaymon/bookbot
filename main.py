from stats import get_words_count
from stats import get_chars_count
from stats import sort_dictionary



def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents


def main():
    import sys 
    arguments = sys.argv
    if len(arguments) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = arguments[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    text = get_book_text(path)
    word_count = get_words_count(text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    char_count = get_chars_count(text)
    print("--------- Character Count -------")
    
    sorted_chars = sort_dictionary(char_count)  

    # Fancy printing
    for entry in sorted_chars:
        char = entry["char"]
        num = entry["num"]
        print(f"{char}: {num}")

    print("============= END ===============")



if __name__ == "__main__":
    main()
