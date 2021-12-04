# -*- coding: utf-8 -*-
from typing import List


class Bingo(object):
    def __init__(self, table):
        self.table = table
        
    def mark(self, n):
        for i in range(len(self.table)):
            for j in range(len(self.table[i])):
                if self.table[i][j] == n:
                   self.table[i][j] = True
    
    def completed(self) -> bool:
        for i in range(len(self.table)):
            if all(x is True for x in self.table[i]):
                return True
            
        for col in range(len(self.table[0])):
            for i in range(len(self.table)):
                if self.table[i][col] is not True:
                    break
            else:
                return True
        return False
    
    def sum(self):
        s = 0
        for row in self.table:
            for col in row:
                if col is not True:
                    s += int(col)
        return s
    

def main():
    with open("d4/input.txt", "r") as f:
        content = f.read()
    
    lines = [x.strip() for x in content.splitlines()]
    t = []
    numbers = lines[0].split(",")
    boards: List[Bingo] = []
    
    for line in lines[2:]:
        if not line:
            if t:
                boards.append(Bingo(t))
                t = []
            continue
        
        t.append(line.replace("  ", " ").split(" "))
    stopped_at = numbers[0]
    for n in numbers:
        remove = []
        for i, board in enumerate(boards):
            board.mark(n)
            if board.completed():
                remove.append(i)
        for v in sorted(remove, reverse=True):
            if len(boards) == 1:
                break
            boards.pop(v)
        if len(boards) == 1:
            stopped_at = n
            break
    
    last = boards[0]
    for n in numbers[numbers.index(stopped_at) + 1:]:
        last.mark(n)
        if last.completed:
            return n, last.sum(), int(n) * last.sum()
        
        
            

if __name__ == "__main__":
    res = main()
    print(res)