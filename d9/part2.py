# -*- coding: utf-8 -*-
from functools import cache
from typing import List, Tuple


def solve(lines: List[str]):
    field = [[int(x) for x in list(line)] for line in lines]
    basins = find_basins(field)
    sizes = [count_neighbours(basin, field) for basin in basins]
    return prod(sorted(sizes, reverse=True)[:3])

def prod(i):
    s = i[0]
    for v in i[1:]:
        s *= v
    return s

def count_neighbours(basin: Tuple[int, int], field, counted=None):
    anz = 0
    x, y = basin
    h = field[y][x]
    if counted is None:
        counted = {(x, y)}

    for d in (-1, 1):
        # x-axis
        if (
            valid_field(x + d, y, field)
            and (x + d, y) not in counted
            and field[y][x + d] == h + 1
            # and field[y][x + d] < 9
        ):
            counted.add((x + d, y))
            anz += count_neighbours((x + d, y), field, counted)
        if (
            valid_field(x, y + d, field)
            and (x, y + d) not in counted
            and field[y + d][x] == h + 1
            # and field[y + d][x] < 9
        ):
            counted.add((x, y + d))
            anz += count_neighbours((x, y + d), field, counted) 

    return anz + 1
                
                



def find_basins(field): 
    for y in range(len(field)):
        for x in range(len(field[y])):
            l = field[y][x]
            values = []
            for d in [1, -1]:
                if valid_field(x, y + d, field):
                    values.append(field[y + d][x])
                if valid_field(x + d, y, field):
                    values.append(field[y][x + d])
                    
            if l < min(values):
                yield x, y


def valid_field(x, y, f):
    return 0 <= x < len(f[0]) and 0 <= y < len(f)


def main(filename):
    with open(filename, "r") as f:
        return solve(f.read().splitlines())

if __name__ == "__main__":
    # print(main("d9/example.txt"))
    # print(main("d9/input.txt"))
    print(main("d9/ex2.txt"))