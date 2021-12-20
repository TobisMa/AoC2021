from typing import List


def solve(data: List[str]):
    algo = data[0]
    image = [list(line) for line in data[1:] if line]
    outside = "."
    for _ in range(2):
        image, outside = transcribe(image, algo, outside)
        # print('\n'.join("".join(l) for l in image))
        # print()
    c = 0
    for y in range(len(image)):
        for x in range(len(image[y])):
            if image[y][x] == "#":
                c += 1
    return c
    

def transcribe(image: List[List[str]], algo, outside):
    new = []
    for y in range(-1, len(image) + 2):
        new.append([])
        for x in range(-1, len(image[0]) + 2):
            new[-1].append(get_pixel(image, (x, y), algo, outside))
    outside = algo[0] if outside == "." else algo[-1]
    return new, outside
    

def get_pixel(image: List[List[str]], pos, algo, outside):
    number = ''.join(get_relevant(pos, image, outside))
    bi = "".join("1" if c == "#" else "0" for c in number)
    return algo[int(bi, 2)]
    

def get_relevant(pos, image, outside):
    x, y = pos
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if 0 <= x + dx < len(image[0]) and 0 <= y + dy < len(image):
                yield image[y + dy][x + dx]
            else:
                yield outside
    
    
def main(filename: str):
    with open(filename, 'r') as f:
        print(solve(f.read().splitlines()))
    

if __name__ == '__main__':
    main("d20/input.txt")
    # main("d20/example.txt")