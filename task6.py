def find(word, letter, start_index):
    count = 0

    while start_index < len(word):
        if word[start_index] == letter:
            count = count + 1
        start_index = start_index + 1
    return count

print(find("banana", "a", 2))