"""
this module generates a list of ulam_numbers in a specific range
"""
def generate_lst(num):
    """
    int -> lst
    returns a list of ulam numbers in a given range num
    >>> generate_lst(100)
    [1, 2, 3, 4, 6, 8, 11, 13, 16, 18, 26, 28, 36, 38, 47, 48, 53, 57,\
 62, 69, 72, 77, 82, 87, 97, 99]
    >>> generate_lst(10)
    [1, 2, 3, 4, 6, 8]

    """
    ulam_lst = [1, 2]
    while ulam_lst[-1] <= num:
        next_ulam = ulam_lst[-1] + ulam_lst[-2]
        sum_lst = []

        for num1 in ulam_lst:
            for num2 in ulam_lst:
                if (num1 != num2) and (num2 > num1):
                    sum_lst.append(num1 + num2)
        # creates sum_lst of all possible sums of pairs of values in ulam_lst

        for sum12 in sum_lst:
            if sum_lst.count(sum12) == 1:
                if (sum12 > ulam_lst[-1]) and (sum12 < next_ulam):
                    next_ulam = sum12
        # searches for the minimal sum in sum_lst that is bigger than the
        # last element in ulam_lst

        ulam_lst.append(next_ulam)
    ulam_lst.pop(-1) 
    # deletes the last value in the ulam_lst, because it's bigger than 
    # the num value beacause of the conditions for the main while cycle
    return ulam_lst
