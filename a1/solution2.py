from typing import List


def check(d):
    d = [int(x) for x in d.splitlines() if x]
    sums = [sum(d[i:i+3]) for i in range(len(d)-2)]
    inc = 0
    for i in range(1, len(sums)):
        if sums[i] > sums[i-1]:
            inc += 1
            print(sums[i], sums[i-1])
    return inc
        

if __name__ == "__main__":
    i = ""
    c = None
    while c != "":
        c = input()
        i += c + "\n"
    print(check(i))