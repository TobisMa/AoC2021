from typing import Dict, Iterable, List, Set
import sys
from itertools import permutations


def solve(lines: List[str]):
    display = {'abcefg': '0', 'cf': '1', 'acdeg': '2', 'acdfg': '3', 'bcdf': '4', 'abdfg': '5', 'abdefg': '6', 'acf': '7', 'abcdefg': '8', 'abcdfg': '9'}

    total = 0
    
    for line in lines:
        seq, output = line.strip().split('|')
        seq = [set(x) for x in seq.strip().split()]
        output = [set(x) for x in output.strip().split()]
        mapping = dict(zip("abcdefg", "abcdefg"))  #  to get rid of UnboundLocalError

        for p in permutations("abcdefg"):
            mapping = dict(zip(p, "abcdefg"))
            for o in seq:
                dig = ''.join(sorted(mapping[c] for c in o))
                if dig not in display:
                    break
                
            else:
                break

        total += int(''.join(
            display[
                ''.join(sorted(mapping[c] for c in o))
            ] 
            for o in output
        ))

    return total


def main(filename):
    with open(filename, "r") as f:
        return solve(f.read().splitlines())


if __name__ == "__main__":
    # print(main("d8/example.txt"))
    print(main("d8/input.txt"))
