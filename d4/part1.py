# -*- coding: utf-8 -*-

class BingoField():
    def __init__(self, table):
        self.table = table
        self.last_num = -1000
    
    def mark(self, n):
        self.last_num = n
        for i in range(len(self.table)):
            for j in range(len(self.table[i])):
                if self.table[i][j] == n:
                    self.table[i][j] = True
                    
    def check(self):
        for row in self.table:
            if all([x is True for x in row]):
                return True
        
        for i in range(len(self.table[0])):
            col = 0
            for j in range(len(self.table)):
                if self.table[j][i] is True:
                    col += 1
            if col == len(self.table[0]):
                return True
        return False
    
    def f_sum(self):
        nsum = 0
        for row in self.table:
            for c in row:
                if c is not True:
                    nsum += int(c)
        
        return nsum



def solve(data):
    numbers = data[0].split(",")
    t = []
    bs = []
    for line in data[2:]:
        if not line:
            if t:
                bs.append(BingoField(t))
                t = []
            continue
        if line.startswith(" "): line = line[1:]
        a = line.replace("  ", " ").split(" ")
        t.append(a)
    
    bs.append(BingoField(t))
    
    winner = None
    for n in numbers:
        for b in bs:
            b.mark(n)
            if b.check():
                winner = b
                break
        if winner is not None:
            break
    if winner is None:
        return -1
    
    return winner.f_sum(), int(winner.last_num), winner.f_sum() * int(winner.last_num)

def main():
    with open("d4/input.txt") as f:
        res = solve(f.read().splitlines())
    print(res)

if __name__ == "__main__":
    main()