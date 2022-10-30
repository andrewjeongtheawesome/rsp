import random
import math
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


def random_choice() -> int:
    return random.randrange(0,3)


def probability():
    global com_pro
    com_pro = 0
    com_pro = int(input("컴퓨터의 승률을 입력하세요.(단위:%,범위:0~100)"))/100
    print("입력 완료 되었습니다.")


def random_choice_probability(a: Hand) -> int:
    left=round(((1-com_pro)/2),1)
    if a==0:
        char_choice=random.choices(range(0,3),weights=[left,com_pro,left],k=1)
        return char_choice[0]
    elif a==1:
        char_choice=random.choices(range(0,3),weights=[left,left,com_pro],k=1)
        return char_choice[0]
    elif a==2:
        char_choice=random.choices(range(0,3),weights=[com_pro,left,left],k=1)
        return char_choice[0]
