# inputs: two lists
# limit
# weights (list) - item weights

# output
# tuple - two items (a, b) where:
# weights[a] + weights[b] = limit
# a is the higher value
# if no pair exists, return None

def get_indices_of_item_weights(weights, length, limit):
    # memoization - store each weight in dict with
    # key: weight (from weight list)
    # value: weight index
    weights_dict = {weight: index for index, weight in enumerate(weights)}
    # loop through weights
    for index, weight in enumerate(weights):
        # weight_2 is the weight which combines with the current weight to equal the limit
        weight_2 = limit - weight
        # if it exists
        if weight_2 in weights_dict:
            # return the indexes of the two weights in specified order
            indexes_list = [index, weights_dict[weight_2]]
            indexes_list.sort(reverse=True)
            return indexes_list
    return None


weights = [4, 6, 10, 15, 16]
length = 5
limit = 21

print(get_indices_of_item_weights(weights, length, limit))
