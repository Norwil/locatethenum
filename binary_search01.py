#Here's an implementation of binary search for solving the problem.

def find_the_num(numbers, query):
    small, big = 0, len(numbers) - 1

    while small <= big:
        mid = (small + big) // 2
        mid_number = numbers[mid]

        print("small:", small, ", big:", big, ", mid:", mid, ", mid_number:", mid_number)

        if mid_number == query:
            return mid
        elif mid_number < query:
            big = small -1
        elif mid_number > query:
            small = big + 1

    return -1
