from typing import List


def hits_target_area(vx, vy, rx, ry):
    posx = posy = 0
    while posx <= max(rx) and posy >= min(ry):
        posx += vx
        posy += vy
        vx -= 0 if vx <= 0 else 1
        vy -= 1
        if posx in rx and posy in ry:
            return True
    return False


def solve(data: List[str]):
    xarea, yarea = data[0].removeprefix("target area: ").split(", ")
    argsx = [int(x) for x in xarea.removeprefix("x=").split("..")]
    argsx[1] += 1
    rx = range(*argsx + [1])
    
    argsy = [int(y) for y in yarea.removeprefix("y=").split("..")]
    argsy[1] += 1
    ry = range(*argsy + [1])
    
    vx = round(max(rx) / 2)
    vy = -min(ry)
    possible = set()
    while vx > 0:
        if hits_target_area(vx, vy, rx, ry):
            possible.add((vx, vy))
        vy -= 1
        if vy == 0:
            vx -= 1
            vy = -min(ry.start, ry.stop)
    vy = max(y for x, y in possible)
    for x, y in possible:
        if y == vy:
            print(x, y)
    y = 0
    heights = set()
    while y not in ry:
        y += vy
        vy -= 1
        heights.add(y)
    return max(heights)
        
        
    
def main(filename: str):
    with open(filename, 'r') as f:
        print(solve(f.read().splitlines()))
    

if __name__ == '__main__':
    # main("d17/input.txt")
    main("d17/example.txt")