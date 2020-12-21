"""
this module tells if a specific number is happy and generating a list
of happy numbers
"""
def is_happy(num):
    """
    int -> boolean
    Tells user whether the n number is happy or not
    >>> is_happy(32)
    True
    >>> is_happy(33)
    False
    """
    num = str(num)
    iter_lst = []  # list of products
    # list of products is used to figure out if by deciding if a num is happy
    # we encounter an endless cycle
    # for example 14 -> 17 -> 50 -> 25 -> 29 -> 85 -> !89! -> 145 -> 42 -> 20
    #  -> 4 -> 16 -> 37 -> 58 -> !89! and so the loop is cycled
    while num not in iter_lst:
        # iter_lst.append(num)
        n1 = 0  # the product of all digits in a number so far
        for i in num:
            n1 += int(i)**2
        num = str(n1)
    if num == 1:
        break
    answer = (num == '1')
    return answer


def generate_lst(len):
    """
    int -> lst
    return a list of happy numbers in a given range
    >>> generate_lst(100)
    [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97]

    """
    happy_lst = []
    for num in range(len):
        if is_happy(num):
            happy_lst.append(num)
    return happy_lst
