# rsp

> 파이썬 가위바위보 라이브러리

가위바위보 기능을 파이썬에서 라이브러리로 이용할 수 있도록 개발되었습니다.
## 기능

### 상수

#### `Hand`

가위바위보 수 타입

* `ROCK` 가위바위보 중 '바위' 수를 의미한다
* `SCISSORS` 가위바위보 중 '가위' 수를 의미한다
* `PAPER` 가위바위보 중 '보' 수를 의미한다

#### `Language`

변환 가능한 언어

* `KOREAN` 한국어 (기본값)
* `MGB` 한국어 (묵찌빠)
* `ENGLISH` 영어
* `JAPANESE` 일본어
* `CHINESE` 중국어

### 함수

```python
is_a_winning_b(a: Hand, b: Hand) -> bool
```

`a`가 `b`를 이기는 수인지 확인하는 함수

```python
is_a_losing_b(a: Hand, b: Hand) -> bool
```

`a`가 `b`를 지는 수인지 확인하는 함수

```python
is_a_equal_b(a: Hand, b: Hand) -> bool
```

`a`와 `b`가 비겼는지 확인하는 함수

```python
stringify(hand: Hand, language: Language) -> str
```

`hand`를 `language` 언어로 변환하여 출력해주는 함수

```python
hand_convert(string: str) -> Hand
```
사용자 입력을 `Hand` 타입으로 바꿔주는 함수

```python
random_choice() -> Hand
```

`ROCK`, `SCISSORS`, `PAPER`중 하나를 랜덤으로 골라서 출력하는 함수

```python
probability(pro: float)
```

`random_choice_probability` 함수의 확률을 결정하는 함수

```python
random_choice_probability(a: Hand) -> Hand
```

`a`의 확률에 가중치를 부여하여 랜덤으로 골라 출력하는 함수
