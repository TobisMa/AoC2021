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
        sent_seq = list(map(set, sl[0].split()))
        out_seq = list(map(set, sl[1].split())) 
        
        for permutation in permutations("abcdefg"):
            mapping = {l: permutation[i] for i, l in enumerate("abcdefg")}
            for s in sent_seq:
                digit = ""
                for l in s:
                    digit += mapping[l]
                
                digit = ''.join(sorted(list(digit)))
                
                if digit not in NUMBERS:
                    break
            else:
                break
        else:
            return "Wtf"
        
        number = ""
        for o in out_seq:
            d = ""
            for l in o:
                d += mapping[l]
            d = ''.join(sorted(list(d)))
            n = NUMBERS.index(d)
            number += str(n)
            
        total += int(number)


    return total


def main(filename):
    with open(filename, "r") as f:
        return solve(f.read().splitlines())


if __name__ == "__main__":
    # print(main("d8/example.txt"))
    print(main("d8/input.txt"))
