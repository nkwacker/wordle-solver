from typing import Set


def load_dictionary(dict_fpath: str = "wordle_complete_dictionary.txt") -> Set[str]:
    d = []
    with open(dict_fpath) as f:
        for x in f.readlines():
            d.append(x.strip())
    return set(d)
