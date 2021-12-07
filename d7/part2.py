from typing import List


def solve(data: List[str]):
    ...


def main(filename):
    with open(filename, "r") as f:
        return solve(f.read().splitlines())        
    
    

if __name__ == "__main__":
    print(main("example.txt"))
    # print(main("input.txt"))