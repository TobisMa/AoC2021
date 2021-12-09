def solve(data): 
    field = [[int(x) for x in list(line)] for line in data]
    res = []
    for y in range(len(field)):
        for x in range(len(field[y])):
            l = field[y][x]
            values = []
            for d in [1, -1]:
                try:
                    values.append(field[y + d][x])
                except IndexError:
                    pass
                try:
                    values.append(field[y][x + d])
                except IndexError:
                    pass
            if l < min(values):
                print(x, y)
                res.append(l + 1)
    return sum(res)
        
        
    
    
    
if __name__ == '__main__':
    with open("d9/input.txt", "r") as f:
        print(solve(f.read().splitlines()))