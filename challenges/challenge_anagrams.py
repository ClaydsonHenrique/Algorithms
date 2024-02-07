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

    if not first_string or not second_string:
        return False

    sorted_first = sort_string(first_string)
    sorted_second = sort_string(second_string)

    return (
        sorted_first,
        sorted_second,
        sorted_first.lower() == sorted_second.lower(),
    )


print(is_anagram("", "perda"))
