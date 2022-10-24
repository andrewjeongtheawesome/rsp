ROCK = 0
SCISSORS = 1
PAPER = 2


def is_a_winning_b(a, b):
    return (a - b) % 3 == 2


def is_a_equal_b(a, b):
    return a == b
