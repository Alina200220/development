from games.nok import nok_game
from games.progression import geometry_progression
from source import GameInteface


def main():
    GameInteface.game_interface(
    "Find the smallest common multiple of given numbers.", nok_game
    )
    GameInteface.game_interface(
        "What number is missing in the progression?", geometry_progression
    )

if __name__ == "__main__":
    main()