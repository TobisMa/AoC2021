# -*- coding: utf-8 -*-
flashs = 0
flashed = set()

def solve(lines):
    global flashed
    field = [[int(c) for c in line] for line in lines]
    t = 0
    while True:
        flashed = set()
        for i in range(len(field)):
            field[i] = [x + 1 for x in field[i]]
        
        for y in range(len(field)):
            for x in range(len(field[0])):
                if field[y][x] >= 10:
                    flash(x, y, field)
        
        n = field[0][0]
        failed = False
        for y in range(len(field)):
            for x in range(len(field[0])):
                if field[y][x] != n:
                    failed = True
                    break
            if failed:
                break
        else:
            return t - n + 1

        t += 1
                
        
    # return flashs
                
def flash(x, y, field):
    global flashs, flashed
    if (x, y) in flashed:
        return
    flashs += 1
        
    field[y][x] = 0
    flashed.add((x, y))
    adjacent = get_adjacent(x, y, field)
    
    for ax, ay in adjacent:
        if (ax, ay) not in flashed:
            field[ay][ax] += 1
            if field[ay][ax] >= 10:
                flash(ax, ay, field)


def get_adjacent(x, y, field):
    points = set()
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            if 0 <= x + dx < len(field[0]) and 0 <= y + dy < len(field):
                points.add((x + dx, y + dy))
    return points


def main():
    # with open("d11/example.txt") as f:
    #     print(solve(f.read().splitlines()))
    with open("d11/input.txt") as f:
        print(solve(f.read().splitlines()))

if __name__ == "__main__":
    main()