from typing import List


class Line:
    max_x = 1
    max_y = 1
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        
    @classmethod
    def from_strings(cls, start, end):
        x1, y1 = start.split(',')
        x2, y2 = end.split(',')
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        
        if max(x1, x2) > Line.max_x:
            Line.max_x = max(x1, x2)
        if max(y1, y2) > Line.max_y:
            Line.max_y = max(y1, y2)
            
        return cls(x1, y1, x2, y2)


class Area(object):
    def __init__(self, lines: List[Line]):
        self.lines = lines
        self.area: List[List[str]] = []
        for _ in range(Line.max_y + 1):
            self.area.append([])
            for _ in range(Line.max_y + 1):
                self.area[-1].append(".")

        for line in lines:
            x1, x2 = line.x1, line.x2
            y1, y2 = line.y1, line.y2
            

            # x-Axis
            for i in range(min(x1, x2), max(x1, x2) + 1):
                if y1 != y2:
                    break  # ignore non-vertically line
                v = self.area[y1][i]
                v = "1" if v == "." else str(int(v) + 1)
                self.area[y1][i] = v
                
            # y-Axis
            for i in range(min(y1, y2), max(y1, y2) + 1):
                if x1 != x2:
                    break
                v = self.area[i][x1]
                v = "1" if v == "." else str(int(v) + 1)
                self.area[i][x1] = v
            
    
    def print(self):
        print('\n'.join(''.join(x) for x in self.area))
        
    def get_dangerous_vents(self):
        for y in range(len(self.area)):
            for x in range(len(self.area[y])):
                if self.area[y][x] != "." and int(self.area[y][x]) >= 2:
                    yield x, y
        

def solve(data: List[str]):
    segments: List[Line] = []
    for line in data:
        start, end = line.split(" -> ")
        segments.append(Line.from_strings(start, end))
    
    a = Area(segments)
    a.print()
    c= 0
    for p in a.get_dangerous_vents():
        c += 1
        print(p, end="; ")
    print()
    return c


def main(filename):
    with open(filename, "r") as f:
        return solve(f.read().splitlines())        
    
    

if __name__ == "__main__":
    # print(main("d5/example.txt"))
    print(main("d5/input.txt"))