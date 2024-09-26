from typing import Callable

from games import nok_game


class Game:
    
    @staticmethod
    def greeting():
        print("Welcome to the Brain Games! ")
        print("May I have your name?")
        name = input()
        print(f"Hello {name}!")
        return name
    
    @staticmethod
    def game_interface(game_description:str, game_fuction:Callable):
        """Общий интерфейс для всех игр, сама функции игры передается аргументом и вызывается в 21 строчке"""
        user_name = Game.greeting()
        print(game_description)
        for i in range(3):
            question_string, correct_answer = game_fuction()
            print(f"Question: {question_string}")
            user_answer = input()
            print(f"Your answer: {user_answer}")
            if int(user_answer) == int(correct_answer):
                print("Correct!")
            else:
                print(f"{user_answer} is wrong answer ;(. Correct answer was {correct_answer}.")
                if i < 2:
                    print(f"Let's try again, {user_name}")

Game.game_interface("Find the smallest common multiple of given numbers.", nok_game)
    
