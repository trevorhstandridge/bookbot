import sys
from stats import get_num_words, count_characters, sorted_character_count

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path_to_file):
    
    with open(path_to_file, 'r') as f:
        return f.read()
    
def main():
    book_text = get_book_text(path_to_file = sys.argv[1])
    word_counts = get_num_words(book_text)
    char_counts = count_characters(book_text)
    sorted_list = sorted_character_count(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f'Found {word_counts} total words')
    print("--------- Character Count -------")
    for entry in sorted_list:
        ch = entry["char"]
        if ch.isalpha():
            print(f"{ch}: {entry['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()