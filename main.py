def main():
    path = "/home/bmitche1/workspace/github.com/bmitche1/bookbot/books/frankenstein.txt"
    #opens file, reads and return number of words
    with open("/home/bmitche1/workspace/github.com/bmitche1/bookbot/books/frankenstein.txt", 'r') as f:
        file_contents = f.read()
    words = file_contents.split()
    word_count = len(words)
   

    #creates dictionary
    letter_dict = {}

    #convert text to lower case and count letters
    for char in file_contents.lower():
        if char.isalpha():
            letter_dict[char] = letter_dict.get(char, 0)  + 1

    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    for letter in sorted(letter_dict):
        print(f"The letter {letter}: {letter_dict[letter]}")
    print("--- end report ---")

if __name__ == "__main__":
    main()
