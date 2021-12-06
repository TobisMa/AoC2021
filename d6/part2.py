from typing import List


def solve(data: str):
    days = 256
    new = 0
    numbers = [int(x) for x in data.split(",")]
    fishs = {i: numbers.count(i)  for i in range(9)}

    for _ in range(days):
        new = fishs[0]

        for timer in range(1, 9):
            fishs[timer - 1] = fishs[timer]

        fishs[6] += new  # reseting timer
        fishs[8] = new  # created fishes at zero counter

    return sum(fishs.values())
        
        
    


def main(filename):
    with open(filename, "r") as f:
        return solve(f.read())       
    
    

if __name__ == "__main__":
    # print(main("d6/example.txt"))
    print(main("d6/input.txt"))