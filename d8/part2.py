from typing import Iterable, List, Set
import sys
from itertools import permutations


NUMBERS = [
    "abcefg",
    "cf",
    "acdeg",
    "acdfg",
    "bcdf",
    "abcdfg",
    "abdefg",
    "acf",
    "abcdefg",
    "abcdfg"
]


def solve(lines):
    total = 0
    for line in lines:
        sl = line.split(" | ")
        seq = list(map(set, sl[0].split()))
        out = list(map(set, sl[1].split())) 

        for p in permutations("abcdefg", r=7):
            mapping = dict(zip(p, "abcdefg"))
            for sent in seq:
                digit = "".join(sorted(mapping[x] for x in sent))
                if digit not in NUMBERS or len(digit) == 7:
                    break
            else:
                break
            
        shown = ""
        mapping = {v: k for k, v in mapping.items()}
        for res in out:
            segments = [mapping[d] for d in res]
            segments.sort()
            shown += str(NUMBERS.index(''.join(segments)))
        total += int(shown)

    return total

def main(filename):
    with open(filename, "r") as f:
        return solve(f.read().splitlines())


if __name__ == "__main__":
    # print(main("d8/example.txt"))
    print(main("d8/input.txt"))
