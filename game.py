from dictionary import load_dictionary
from typing import Optional
import random
from colorama import Fore

EXACT_MATCH = "X"
WRONG_MATCH = "."
NO_MATCH = " "


def get_result(guess: str, solution: str) -> str:
    result = [NO_MATCH] * len(solution)
    letter_used = [False] * len(solution)
    # exact matches
    for i in range(len(solution)):
        if guess[i] == solution[i]:
            result[i] = EXACT_MATCH
            letter_used[i] = True
    # now the wrong matches
    for i in range(len(guess)):
        for j in range(len(solution)):
            if guess[i] == solution[j] and not letter_used[j]:
                letter_used[j] = True
                result[i] = WRONG_MATCH
                break
    return "".join(result)


class Game:
    def __init__(self, turn_limit: int = 6, silent_errors: bool = False, dict_fpath: Optional[str] = None) -> None:
        self._turn_counter = 0
        self._turn_limit = turn_limit
        self._silent_errors = silent_errors
        if dict_fpath is None:
            self._dictionary = load_dictionary()
        else:
            self._dictionary = load_dictionary(dict_fpath=dict_fpath)
        self._solution = random.sample(self._dictionary, k=1)[0]

    def _game_print(self, message: str):
        if not self._silent_errors:
            print(message)

    def _print_match_str(self, guess: str, match_str: str) -> None:
        guess_in_color = ""
        for i in range(len(match_str)):
            if match_str[i] == EXACT_MATCH:
                guess_in_color += Fore.GREEN
            elif match_str[i] == WRONG_MATCH:
                guess_in_color += Fore.YELLOW
            else:
                guess_in_color += Fore.RESET
            guess_in_color += guess[i]
        guess_in_color += Fore.RESET
        self._game_print(guess_in_color)

    def guess(self, word: str) -> Optional[str]:
        if self._turn_counter >= self._turn_limit:
            self._game_print("game is over")
            return None
        word = word.lower()
        if len(word) != 5:
            self._game_print("word must be 5 letters long")
            return None
        if word not in self._dictionary:
            self._game_print("word not in dictionary")
            return
        self._turn_counter += 1
        result_str = get_result(guess=word, solution=self._solution)
        self._print_match_str(guess=word, match_str=result_str)
        return result_str
