from dictionary import load_dictionary
from game import get_result, EXACT_MATCH, WRONG_MATCH, NO_MATCH
from typing import List, Set
import time

from progressbar import Bar, Percentage, ProgressBar


def _pare_solution_set(soltion_set: List[str], guess: str, result: str):
    new_solutions = soltion_set.copy()
    for i in range(len(result)):
        if result[i] == EXACT_MATCH:
            new_solutions = [solu for solu in new_solutions if solu[i] == guess[i]]
        elif result[i] == WRONG_MATCH:
            new_solutions = [solu for solu in new_solutions if solu[i] != guess[i] and guess[i] in solu]
        elif result[i] == NO_MATCH:
            new_solutions = [solu for solu in new_solutions if solu.count(guess[i]) < guess.count(guess[i])]
    return new_solutions


class Solver:
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._total_compute_time = 0
        self._dictionary = load_dictionary()
        self._solution_set = self._dictionary.copy()

    def _get_possible_results(self, guess: str) -> Set[str]:
        return set([get_result(guess, x) for x in self._solution_set])

    def get_next_guess(self) -> str:
        start_time = time.time()
        if len(self._solution_set) == 1:
            print("found the word!")
            print(f"total compute time: {self._total_compute_time} seconds")
            return self._solution_set[0]
        elif len(self._solution_set) == len(self._dictionary):
            return "serai"
        i = 0
        pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=len(self._dictionary)).start()
        guess_set_counts = []
        for guess in self._dictionary:
            i += 1
            pbar.update(i)
            possible_results = self._get_possible_results(guess)
            max_future_solution_set_length = 0
            for result in possible_results:
                future_solution_set_length = len(_pare_solution_set(self._solution_set, guess, result))
                max_future_solution_set_length = max(max_future_solution_set_length, future_solution_set_length)
                if max_future_solution_set_length == len(self._solution_set):
                    break
            guess_set_counts.append((max_future_solution_set_length, guess))
        pbar.finish()
        self._total_compute_time += time.time() - start_time
        min_future_solu_set_size = min(guess_set_counts)[0]
        guess_set = set([x[1] for x in guess_set_counts if x[0] == min_future_solu_set_size])
        guess_solutions = guess_set.intersection(self._solution_set)
        if len(guess_solutions) > 0:
            return next(iter(guess_solutions))
        else:
            return next(iter(guess_set))

    def game_result(self, guess: str, result: str) -> None:
        start_time = time.time()
        if len(guess) != len(result) or len(result) != 5:
            print("5-letter words only")
            return
        self._solution_set = _pare_solution_set(self._solution_set, guess, result)
        print(f"{len(self._solution_set)} solutions remain")
        self._total_compute_time += time.time() - start_time
