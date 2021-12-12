from typing import Generator, List, Set, Tuple


field = []


def solve(lines: List[str]):
    global field
    field = [[int(c) for c in line] for line in lines]
    basins = find_basins(field)
    sizes = []
    
    for b in basins:
        size = measure_size(b, set())
        sizes.append(size)
        
    sizes.sort(reverse=True)
    return prod(sizes[:3])


def measure_size(pos: Tuple[int, int], computed: Set[Tuple[int, int]]) -> int:
    x, y = pos
    ph = field[y][x]
    
    total = 0
    neighbours = get_neighbours(x, y)
    for n in neighbours:
        if n in computed:
            continue
        
        nx, ny = n
        computed.add(n)
        h = field[ny][nx]
        
        if h < 9:
            total += 1
            res = measure_size(n, computed)
            total += res
    
    return total


def find_basins(field: List[List[int]]) -> Generator[Tuple[int, int], None, None]:
    for y in range(len(field)):
        for x in range(len(field[y])):
            neighbour = get_neighbours(x, y)
            values = [field[y][x] for x, y in neighbour]
            
            if field[y][x] < min(values):
                yield x, y
                

def get_neighbours(x: int, y: int) -> Generator[Tuple[int, int], None, None]:
    for d in [-1, 1]:
        if valid_field(x + d, y):
            yield x + d, y
        if valid_field(x, y + d):
            yield x, y + d


def valid_field(x: int, y: int):
    return 0 <= x < len(field[0]) and 0 <= y < len(field)
        
        
def prod(iterable):
    r = 1
    for v in iterable:
        print(v)
        r *= v
    return r


def main(filename):
    with open(filename) as f:
        print(solve(f.read().splitlines()))


if __name__ == "__main__":
    main("d9/input.txt")
    # main("d9/ex2.txt")
    # main("d9/example.txt")