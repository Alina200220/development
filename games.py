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


def geometry_progression() -> Tuple[str, int]:
    """Логика игры геометрическая прогрессия"""
    q = randint(1, 10)  # знаменатель прогрессии
    b_first = randint(1, 10)  # первый элемент прогрессии
    progression_elements = [b_first]
    for i in range(1, 10):
        progression_elements.append(
            progression_elements[i - 1] * q
        )  # геометрическая прогрессия из 10 элементов
    index_of_element_to_replace = randint(0, 9)
    correct_answer = progression_elements[index_of_element_to_replace]
    progression_elements[index_of_element_to_replace] = ".."
    question_string = " ".join(list(map(str, progression_elements)))
    return question_string, correct_answer
