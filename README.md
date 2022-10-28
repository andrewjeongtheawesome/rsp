# rsp

> 파이썬 가위바위보 라이브러리

파이썬에서 가위바위보를 쉽게 구현할 수 있도록 합니다.
## 기능

### 상수

* `Hand` 가위바위보 수 타입

* `ROCK` 가위바위보 중 '바위' 수를 의미한다
* `SCISSORS` 가위바위보 중 '가위' 수를 의미한다
* `PAPER` 가위바위보 중 '보' 수를 의미한다

### 함수

```python
is_a_winning_b(a: Hand, b: Hand) -> bool
```

`a`가 `b`를 이기는 수인지 확인하는 함수

```python
is_a_equal_b(a: Hand, b: Hand) -> bool
```

`a`와 `b`가 비겼는지 확인하는 함수

```python
stringify(hand: Hand) -> str
```

`hand`를 한국어로 변환하여 출력해주는 함수

