def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False
    if not word or low_index >= high_index:
        return True
    if word[low_index] != word[high_index]:
        return False

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
