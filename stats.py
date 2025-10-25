
def get_num_words(book_text):
    
    num_words = 0
    word_split = book_text.split()
    
    for word in word_split:
        num_words += 1
    
    return num_words

def count_characters(book_text):
    
    char_counts = {}

    for char in book_text.lower():
        char_counts[char] = char_counts.get(char, 0) + 1
 
    return char_counts

def sort_on(item):
    return item["num"]

def sorted_character_count(char_counts):
    
    sorted_list = []

    for char, num in char_counts.items():
        sorted_list.append({"char": char, "num": num})
    
    sorted_list.sort(reverse=True, key=sort_on)
    
    return sorted_list