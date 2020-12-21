"""
this module generates lists of lucky numbers
"""
def generate_lst(num):
    """
    int -> list
    creates a list of lucky numbers in a given range num
    >>> generate_lst(100)
    [1, 3, 7, 9, 13, 15, 21, 25, 31, 33, 37, 43, 49, 51, 63, 67,\
 69, 73, 75, 79, 87, 93, 99]
    >>> generate_lst(10)
    [1, 3, 7, 9]

    """
    lst = list(range(1, num + 1, 2))
    lucky_lst = [lst[0]]
    k = 1
    while True:
        try:
            lucky_lst.append(lst[k])  # we add the next number from lst as is stated in lucky sieve algorithm
            j = 0
            remove_list = []
            while True:
                try:
                    if (j >= lst[k]) and (j % lst[k] == 0):
                        remove_list.append(lst[j - 1])
                    j += 1
                except (IndexError, ValueError):
                    break
            # we create the remove_lst of all values that can be divided
            # by the last value we added with zero remainder

            for i in remove_list:
                lst.remove(i)
            # we remove all values of remove_lst from initial lst
            k += 1
        except IndexError:
            break
    return lucky_lst

print(generate_lst(10))