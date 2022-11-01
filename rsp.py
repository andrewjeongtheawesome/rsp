import random
Hand = int

ROCK = 0
SCISSORS = 1
PAPER = 2


def is_a_winning_b(a: Hand, b: Hand) -> bool:
    return (a - b) % 3 == 2


def is_a_equal_b(a: Hand, b: Hand) -> bool:
    return a == b


KOREAN_TABLE = {ROCK: '바위', PAPER: '보', SCISSORS: '가위'}


def stringify(hand: Hand) -> str:
    return KOREAN_TABLE[hand]


def random_choice() -> Hand:
    return random.randrange(0, 3)


com_pro = 1/3


def probability(input):
    global com_pro
    com_pro = input


def random_choice_probability(a: Hand) -> int:
    left = round(((1 - com_pro) / 2), 1)
    my_weights = list()

    if a == 0:
        my_weights = [left, com_pro, left]
    elif a == 1:
        my_weights = [left, left, com_pro]
    elif a == 2:
        my_weights = [com_pro, left, left]

    char_choice = random.choices(range(0, 3), weights=my_weights, k=1)
    return char_choice[0]
