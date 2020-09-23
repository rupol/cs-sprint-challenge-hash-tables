# input: list of lists of integers
# output: list of numbers that exist in all lists (intersection)

def intersection(arrays):
    # store integers in dict
    # key: integer
    # value: number of times integer has been "seen" (number of arrays it's in)
    integer_counts = {}
    for array in arrays:
        for num in array:
            if num not in integer_counts:
                integer_counts[num] = 1
            else:
                integer_counts[num] += 1

    result = []
    for num, count in integer_counts.items():
        # if integer is in array.length() arrays, it's in all of them
        if count == len(arrays):
            # add to result
            result.append(num)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

# arrays = [
#     [1, 2, 3, 4, 5],
#     [12, 7, 2, 9, 1],
#     [99, 2, 7, 1, ]
# ]

# print(intersection(arrays))
