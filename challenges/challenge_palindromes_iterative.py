def is_palindrome_iterative(word):
    if word == "":
        return False

    i = list(word)

    for index in range(len(i)):
        if i[index] != i[len(i) - 1 - index]:
            return False
    return True
