def find(word, letter, start_index):



    while start_index < len(word):
        if word[start_index] == letter:
            return start_index
        index = start_index + 1
    return -1


print(find("computer", "p"))
