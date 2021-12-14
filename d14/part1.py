from typing import Dict, List, Tuple


class PolymerTemplate(object):
    def __init__(self, templ: str, rules: List[str]):
        self.templ = templ
        self.rules = {}
        
        for r in rules:
            if not r or " -> " not in r:
                continue
            which, new = r.split(" -> ")
            self.rules[which] = new
        
    def insert(self):
        todo: List[Tuple] = []
        for i in range(len(self.templ) - 1):
            for match, repl in self.rules.items():
                if self.templ[i:i + 2] == match:
                    todo.append((i, repl))
        todo.sort(key=lambda x: x[0], reverse=True)
        for t in todo:
            self.templ = self.templ[:t[0] + 1] + t[1] + self.templ[t[0] + 1:]
            
            
    def repear_insertion(self, times=5):
        for _ in range(times):
            self.insert()
        


def solve(data: List[str]):
    polymer_template = data[0]
    rules = [line for line in data if line]
    pt = PolymerTemplate(polymer_template, rules)
    pt.repear_insertion(2)
    print(pt.templ)
    histo = histogram(pt.templ)
    h = [(k, v) for k, v in histo.items()]
    h.sort(key=lambda x: x[1])
    return h[-1][1] - h[0][1]
    

def histogram(pt) -> Dict[str, int]:
    res = {}
    for k in pt:
        if k not in res.keys():
            res[k] = 0
        res[k] += 1
    return res
    
    
def main(filename: str):
    with open(filename, 'r') as f:
        print(solve(f.read().splitlines()))
    

if __name__ == '__main__':
    main("d14/input.txt")
    # main("d14/example.txt")