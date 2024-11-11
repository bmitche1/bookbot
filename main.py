def main():
    with open("/home/bmitche1/workspace/github.com/bmitche1/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    word_count = len(words)
    print(word_count)
if __name__ == "__main__":
    main()
