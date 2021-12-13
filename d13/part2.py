from typing import List, Set, Tuple


def solve(data: List[str]):
    points: Set[Tuple[int, int]] = {tuple(int(v) for v in x.split(",")) for x in data if x and not x.startswith("fold")}
    stop = data.index("")
    foldings = []
    for line in range(stop + 1, len(data)):
        folding = data[line].split(" ")[-1]
        axis, value = folding.split("=")
        foldings.append((axis, int(value)))
    
    for folding in foldings:
        npoints = fold(folding, points)
        points = npoints
    
    xmax = 0
    ymax = 0
    for p in points:
        x, y = p
        xmax = max(xmax, x)
        ymax = max(ymax, y)
    
    ymax += 1
    xmax += 1
    field = [list(" "*xmax) for y in range(ymax)]
    
    for p in points:
        x, y = p
        field[y][x] = "#"
    
    f = open("part2o.txt", "w")
    for row in field:
        print(' '.join(row), file=f)
    f.close()
    return None
        
def fold(folding, points):
    # sourcery skip: merge-duplicate-blocks, remove-redundant-if, switch
    axis, value = folding
    np = set()
    for point in points:
        x, y = point
        if axis == "x":
            if x <= value:
                np.add((x, y))
            else:
                d = abs(value - x)
                np.add((value - d, y))

        elif axis == "y":
            if y <= value:
                np.add((x, y))
            else:
                d = abs(value - y)
                np.add((x, value - d))
            
    return np


def main(filename: str):
    with open(filename, "r") as f:
        print(solve(f.read().splitlines()))


if __name__ == "__main__":
    main("d13/input.txt")
    # main("d13/example.txt")