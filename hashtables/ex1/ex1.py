def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    hash_map = {}
    for index, weight in enumerate(weights):
        if weight in hash_map:
            hash_map[weight].insert(0, index)
        else:
            hash_map[weight] = [index]

    for key in hash_map:
        if limit-key in hash_map:
            # handling special case for identical weights
            if key == limit-key:
                return tuple(hash_map[key])
            ans = tuple(
                sorted([hash_map[key][0], hash_map[limit-key][0]], reverse=True))
            print(ans)
            return ans


print(get_indices_of_item_weights([4, 4], 2, 8))
