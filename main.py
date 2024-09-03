with open("./books/frankenstein.txt") as f:
    file_contents = f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    count = {}
    for char in text.lower():
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

def sort_on(dict):
    return dict["num"]


def main():
    char_count = count_characters(file_contents)
    word_count = count_words(file_contents)
    char_list = []
    for char, count in char_count.items():
        if char.isalnum():
            char_list.append({"char": char, "num": count})
    char_list.sort(key=lambda x: x["num"], reverse=True)
    print(f"Total word count: {word_count}")
    print("--- Top 10 most common characters ---")
    for item in char_list[:10]:
        print(f"The '{item['char']}' character was found {item['num']} times")



main()
