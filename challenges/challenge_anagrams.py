def sort_string(string):
    if len(string) <= 1:
        return string
    else:
        middle = len(string) // 2
        left_half = sort_string(string[:middle])
        right_half = sort_string(string[middle:])
        return merge(left_half, right_half)


def merge(left, right):
    result = ""
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index].lower() <= right[right_index].lower():
            result += left[left_index]
            left_index += 1
        else:
            result += right[right_index]
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result


def is_anagram(first_string, second_string):
    first_string = sort_string(first_string.lower())
    second_string = sort_string(second_string.lower())
    if not first_string or not second_string:
        result = (first_string, second_string, False)
        return result
    if first_string == second_string:
        result = (first_string, second_string, True)
        return result
    return (first_string, second_string, False)
