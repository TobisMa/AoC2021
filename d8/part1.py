from typing import List

ONE = 2
FOUR = 4
SEVEN = 3
EIGHT = 7


def solve(data: List[str]):
    output = [x.split('|')[1] for x in data]
    counter = {
        1: 0,
        4: 0,
        7: 0,
        8: 0
    }
    for o in output:
        nums = o.split(" ")
        for n in nums:
            segments = len(n)
            if segments == ONE:
                counter[1] += 1
            elif segments == FOUR:
                counter[4] += 1
            elif segments == SEVEN:
                counter[7] += 1
            elif segments == EIGHT:
                counter[8] += 1
    return sum(counter.values())


def main(filename):
    with open(filename, "r") as f:
        return solve(f.read().splitlines())        
    
    

if __name__ == "__main__":
    # print(main("d8/example.txt"))
    print(main("d8/input.txt"))