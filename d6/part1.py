from typing import List


class Lanternfish:
    
    fishs = []
    to_add = []
    
    def __init__(self, day: int, initialze: bool = False):
        self.day = day
        self.timer = self.day
        if initialze:
            Lanternfish.fishs.append(self)
        
    def __repr__(self) -> str:
        return str(self.timer)
    
    def tick(self, day):
        self.timer -= 1
        if self.timer < 0:
            # print(day)
            self.timer = 6
            self.to_add.append(Lanternfish(8))
            
    @staticmethod
    def number():
        return len(Lanternfish.fishs)


def solve(data: str):
    numbers = data.split(",")
    for n in numbers:
        Lanternfish(int(n), True)
    
    for i in range(1, 81):
        for fish in Lanternfish.fishs:
            fish.tick(i)
        Lanternfish.fishs.extend(Lanternfish.to_add)
        Lanternfish.to_add = []
        # print(', '.join(repr(l) for l in Lanternfish.fishs))
        
    return Lanternfish.number()


def main(filename):
    with open(filename, "r") as f:
        return solve(f.read())        
    
    

if __name__ == "__main__":
    # print(main("d6/example.txt"))
    print(main("d6/input.txt"))