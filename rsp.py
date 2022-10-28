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
MGB_TABLE = {ROCK: '묵', PAPER: '빠', SCISSORS: '찌'}
ENGLISH_TABLE = {ROCK: 'ROCK', PAPER: 'PAPER', SCISSORS: 'SCISSORS'}


def stringify_korean(hand: Hand) -> str:
    return KOREAN_TABLE[hand]


def stringify_mgb(hand: Hand) -> str:
    return MGB_TABLE[hand]


def stringify_english(hand: Hand) -> str:
    return ENGLISH_TABLE[hand]

def random_choice() -> int:
    return random.randrange(0,3)

