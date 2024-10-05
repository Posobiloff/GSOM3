def find_two_samllest(numbers):
    """This function finds the two smallest values in the list of integers"""
    two_smallest = sorted(numbers)
    return (two_smallest[0], two_smallest[1])