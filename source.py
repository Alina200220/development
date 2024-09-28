from typing import Callable

#from games import geometry_progression, nok_game


class GameInteface:
    @staticmethod
    def greeting():
        print("Welcome to the Brain Games! ")
        print("May I have your name?")
        name = input()
        print(f"Hello {name}!")
        return name

    @staticmethod
    def check_answer(correct_answer, user_answer, user_name: str) -> bool:
        """Функция сравнивает правильный ответ и пользователя, выводит соответствующие строки"""
        print(f"Your answer: {user_answer}")
        if int(user_answer) == int(correct_answer):
            print("Correct!")
            return True
        else:
            print(
                f"{user_answer} is wrong answer ;(. Correct answer was {correct_answer}."
            )
            print(f"Let's try again, {user_name}")
            return False

    @staticmethod
    def one_round(user_name: str, game_fuction: Callable) -> bool:
        for j in range(3):
            question_string, correct_answer = game_fuction()
            print(f"Question: {question_string}")
            user_answer = input()
            answer = GameInteface.check_answer(correct_answer, user_answer, user_name)
            if (
                answer is False
            ):  # если пользователь дал неверный ответ, то три раунда заново
                return False
        return True

    @staticmethod
    def game_interface(game_description: str, game_fuction: Callable):
        """Общий интерфейс для всех игр, сама функции игры передается аргументом и вызывается в 36 строчке. Всего три раунда по три вопроса в каждом"""
        user_name = GameInteface.greeting()
        print(game_description)
        for i in range(3):
            win = GameInteface.one_round(user_name, game_fuction)
            if win:
                print("Congratulations!")
                return
        print("You lost 3 rounds")
