from random import randint

def nok_game() -> int:
    """Логика игры по нахождению НОК"""
    def get_nok(a, b):
      c = a * b
      # поиск нод
      while a != 0 and b != 0:
         b, a = max(a, b) % min(a, b), min(a, b)
      return c // (a + b)
    lst = [str(randint(0, 1000)) for _ in range(3)]
    answer = get_nok(int(lst[0]), get_nok(int(lst[1]), int(lst[2])))
    question_string = " ".join(lst)
    return question_string, answer
