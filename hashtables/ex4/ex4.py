# input: list of integers (unordered)
# output: list of the inters in the input that are represented both positively and negatively (i.e. 1 and -1)

def has_negatives(a):
    # store integers in dict
    # key: absolute value
    # value: number of times value has been "seen"
    abs_vals = {}
    for num in a:
        abs_val = abs(num)
        if abs_val not in abs_vals:
            abs_vals[abs_val] = 1
        else:
            abs_vals[abs_val] += 1

    result = []
    for num, count in abs_vals.items():
        # if absolute value has been seen twice, it has both a positive and negative in the original list
        if count > 1:
            # add to result
            result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
