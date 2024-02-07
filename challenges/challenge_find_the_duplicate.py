def find_duplicate(nums):
    number = set()

    for numbers in nums:
        if isinstance(numbers, str):
            return False

        if numbers < 0:
            return False

        if numbers in number:
            return numbers

        number.add(numbers)

    return False
