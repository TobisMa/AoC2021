from collections import defaultdict
from os import replace
from typing import Dict, List, Tuple


class PolymerTemplate(object):
    def __init__(self, templ: str, rules: List[str]):
        self.templ = defaultdict(int)
        self.rules = {}
        self.letters = defaultdict(int)

        for r in rules:
            if not r or " -> " not in r:
                continue
            match, new = r.split(" -> ")
            self.rules[match] = new
            self.templ[match] = int()

        for c in zip(templ, templ[1:]):
            self.templ[''.join(c)] = self.templ[''.join(c)] + 1
            
        for c in templ:
            self.letters[c] = self.letters[c] + 1
        
    def insert(self):
        for seq, occurences in self.templ.items():
            p1, p2 = seq[0] + self.rules[seq], self.rules[seq] + seq[1]
            self.templ[p1] += occurences
            self.templ[p2] += occurences
            self.templ[seq] = 0  # set to zero because no match left after insertion
            
            
    def repear_insertion(self, times=5):
        for _ in range(times):
            self.insert()


def solve(data: List[str]):
    polymer_template = data[0]
    rules = [line for line in data if line]
    pt = PolymerTemplate(polymer_template, rules)
    pt.repear_insertion(10)
    print(pt.templ)
    
    histo = histogram(pt.templ)
    h = [(k, v) for k, v in histo.items()]
    h.sort(key=lambda x: x[1])
    return h[-1][1] - h[0][1]
    
    
def histogram(pt) -> Dict[str, int]:
    res = {}
    for k, v in pt.items():
        k1, k2 = k
        if k1 not in res.keys():
            res[k1] = int()
        res[k1] += v
        if k2 not in res.keys():
            res[k2] = int()
        res[k2] += v
    return res

    
def main(filename: str):
    with open(filename, 'r') as f:
        print(solve(f.read().splitlines()))
    

if __name__ == '__main__':
    # main("d14/input.txt")
    main("d14/example.txt")
    defaultdict()
