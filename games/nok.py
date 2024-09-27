from random import randint
from typing import Tuple


def nok_game() -> Tuple[str, int]:
    """Логика игры по нахождению НОК"""

    def get_nok(a, b):
        c = a * b
        # поиск нод
        while a != 0 and b != 0:
            b, a = max(a, b) % min(a, b), min(a, b)
        return c // (a + b)

    lst = [str(randint(0, 100)) for _ in range(3)]
    answer = get_nok(int(lst[0]), get_nok(int(lst[1]), int(lst[2])))
    question_string = " ".join(lst)
    return question_string, answer