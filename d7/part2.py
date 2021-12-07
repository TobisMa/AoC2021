from typing import List
import time


def solve(data: List[str]):
    numbers = [int(x) for x in data]
    ma = max(numbers)
    mi = min(numbers)
    
    res = {distance: calculate_fuel(numbers, distance) for distance in range(mi, ma)}
    least_key = None
    for key, _ in res.items():
        if least_key is None or res[key] < res[least_key]:
            least_key = key
    if least_key is None:
        return "...."
    return int(res[least_key])
    

def calculate_fuel(numbers, distance):
    fuel = 0
    for pos in numbers:
        n = abs(abs(pos) - distance)
        fuel += ((n + 1) * n) / 2
    return fuel
        


def main(filename):
    with open(filename, "r") as f:
        return solve(f.read().split(","))        
    
    

if __name__ == "__main__":
    # print(main("d7/example.txt"))
    print(main("d7/input.txt"))