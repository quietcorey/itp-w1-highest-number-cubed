"""This is the entry point of the program."""


def highest_number_cubed(limit):
    count = 0
    while count ** 3 < limit:
        count += 1
    return count - 1