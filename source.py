from typing import Callable

from games import geometry_progression, nok_game


class GameInteface:
    
    @staticmethod
    def greeting():
        print("Welcome to the Brain Games! ")
        print("May I have your name?")
        name = input()
        print(f"Hello {name}!")
        return name
    
    @staticmethod
    def check_answer(correct_answer, user_answer, user_name:str, i:int) -> bool:
        """Функция сравнивает правильный ответ и пользователя, выводит соответствующие строки"""
        print(f"Your answer: {user_answer}")
        if int(user_answer) == int(correct_answer):
            print("Correct!")
            return True
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was {correct_answer}.")
            print(f"Let's try again, {user_name}")
            return False

    @staticmethod
    def game_interface(game_description:str, game_fuction:Callable):
        """Общий интерфейс для всех игр, сама функции игры передается аргументом и вызывается в 34 строчке"""
        user_name = GameInteface.greeting()
        print(game_description)
        for i in range(3):
            question_string, correct_answer = game_fuction()
            print(f"Question: {question_string}")
            user_answer = input()
            answer = GameInteface.check_answer(correct_answer, user_answer, user_name, i)
            if not answer: #если пользователь дал неверный ответ, то три раунда заново
                i = 0
        print("Congratulations!")

GameInteface.game_interface("Find the smallest common multiple of given numbers.", nok_game)
GameInteface.game_interface("What number is missing in the progression?", geometry_progression)
    
