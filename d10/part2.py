from typing import List


MACTHING_BRACKETS = {
    "}": "{",
    ")": "(",
    "]": "[",
    ">": "<"
}
RMACTHING_BRACKETS = {v: k for k, v in MACTHING_BRACKETS.items()}

POINTS = {
    "}": 3, 
    ")": 1,
    "]": 2,
    ">": 4
}


def solve(lines: List[str]):
    scores = []
    for line in lines:
        brackets = []
        for character in line:
            if character in MACTHING_BRACKETS.values():
                brackets.append(character)
            elif character in MACTHING_BRACKETS.keys():
                if brackets[-1] == MACTHING_BRACKETS[character]:
                    brackets.pop(-1)
                else:
                    break
        else:
            points = 0
            for left in reversed(brackets):
                points = points * 5 + POINTS[RMACTHING_BRACKETS[left]]
            scores.append(points)
    return sorted(scores)[len(scores) // 2]
    

def main(filename):
    with open(filename, "r") as f:
        return solve(f.readlines())

if __name__ == "__main__":
    # print(main("d10/example.txt"))
    print(main("d10/input.txt"))