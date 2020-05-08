def has_negatives(a):

    """
    YOUR CODE HERE
    """
    positives = {}
    ans = []
    for num in a:
        if abs(num) in positives:
            ans+= [abs(num)]
        else:
            positives[abs(num)] = None
    return ans


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
