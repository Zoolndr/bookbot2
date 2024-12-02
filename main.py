def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        wordcount = get_word_count(file_contents                           )
        sorted_number_record = letter_count(file_contents)
        print(f"--- Begin report of books/frankenstein.txt ---\n {wordcount} words found in the document\n\n")
        for letter, count in sorted_number_record:
            print(f"The {letter} character was found {count} times")
        print("--- End report ---")

def get_word_count(text):
    words = text.split()
    wordcount = len(words)
    return wordcount

def letter_count(text):
    number_record = {}
    text_l = text.lower()
    for c in text_l:
        if c.isalpha():
            if c not in number_record:
                number_record[c] = 1
            else:
                number_record[c] += 1
        sorted_number_record = sorted(number_record.items(), key=lambda item: item[1], reverse=True)
    return sorted_number_record 
    



main()
  