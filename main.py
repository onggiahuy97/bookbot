def count_characters(words):
    d = {}
    for word in words:
        for c in word:
            if c in d:
                d[c] = d[c] + 1
            else:
                d[c] = 1
    return d

def print_report(d):
    for c in d:
        print(f"{c}: {d[c]}")

path_to_file = "bookbot/books/frankenstein.txt"

with open(path_to_file) as f:
    file_contents = f.read().lower()
    words = file_contents.split()
    d = count_characters(words)
    print_report(d)
