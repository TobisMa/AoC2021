from typing import List


MACTHING_BRACKETS = {
    "}": "{",
    ")": "(",
    "]": "[",
    ">": "<"
}

POINTS = {
    "}": 1197, 
    ")": 3,
    "]": 57,
    ">": 25137
}


def solve(lines: List[str]):
    points = []
    for line in lines:
        brackets = []
        for character in line:
            if character in MACTHING_BRACKETS.values():
                brackets.append(character)
            elif character in MACTHING_BRACKETS.keys():
                if brackets[-1] == MACTHING_BRACKETS[character]:
                    brackets.pop(-1)
                else:
                    points.append(POINTS[character])
                    break
    return sum(points)
    

def main(filename):
    with open(filename, "r") as f:
        return solve(f.readlines())

if __name__ == "__main__":
    # print(main("d10/example.txt"))
    print(main("d10/input.txt"))