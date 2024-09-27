from random import randint
from typing import Tuple

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