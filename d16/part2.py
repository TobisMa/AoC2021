from typing import Iterable, List, Optional, Tuple, Union
import json

HEX_TO_BIN = {hex(i)[2:]: "0"*(4-len(bin(i)[2:])) + bin(i)[2:] for i in range(16)}


def flatten(l):
    res = []
    for lst in l:
        res += lst
    return res


def product(iterable: Iterable):
    res = 1
    for i in iterable:
        res *= i
    return res


class Packet:
    def __init__(self, data: str, version: int = -1, type: int = -1, value: str = "", mode: Optional[bool] = None, subpackages: List = None, **optional) -> None:
        self.data = data
        self.version = version
        self.type = type
        self.value = value
        self.mode = mode
        self.subpacke_bits = ""
        self.subpackages: List[Packet] = [] if subpackages is None else subpackages
        self.optional = optional
        self.position = 0
        self.package_end = -1
        
    @property
    def values(self) -> Union[List[int], int]:
        if self.type == 4:
            return int(self.value, 2)
        else:
            return [p.result for p in self.subpackages]  # type: ignore
        
    @property
    def added_versions(self):
        v = self.version
        return v + sum(p.added_versions for p in self.subpackages)
    
    @property
    def result(self):
        if self.type == 0:
            return sum(p.result for p in self.subpackages)
        elif self.type == 1:
            return product(p.result for p in self.subpackages)
        elif self.type == 2:
            return min(p.result for p in self.subpackages)
        elif self.type == 3:
            return max(p.result for p in self.subpackages)
        elif self.type == 4:
            return int(self.value, 2)
        elif self.type == 5:
            return int(self.subpackages[0].result > self.subpackages[1].result)
        elif self.type == 6:
            return int(self.subpackages[0].result < self.subpackages[1].result)
        elif self.type == 7:
            return int(self.subpackages[0].result == self.subpackages[1].result)
        
    @property
    def subpackage_length(self):
        return int(self.subpacke_bits, 2)
        
    def __repr__(self):
        return str(self.__dict__)
    
    def __str__(self):
        return self.__repr__()
    
    def parse(self):
        self.version = int(self.data[:3], 2)
        self.type = int(self.data[3:6], 2)

        self.position = 6
        if self.type == 4:
            for i in range(self.position, len(self.data), 5):
                vp = self.data[i:i+5]
                self.value += vp[1:]
                self.position += 5

                if vp.startswith("0"):
                    break

        else:
            self.mode = self.data[6] == "1"
            self.position += 1

            if self.mode:   # 11 bit
                self.subpacke_bits = self.data[self.position:self.position + 11]
                self.position += 11

                for _ in range(self.subpackage_length):
                    data = self.data[self.position:]
                    if not data.strip("0"):
                        break
                    p = Packet(data)
                    p.parse()
                    self.position += p.package_end
                    self.subpackages.append(p)
            else:   # 15 bit
                self.subpacke_bits = self.data[self.position:self.position + 15]
                self.position += 15
                i = 0
                while i < self.subpackage_length:
                    data = self.data[self.position:self.position + self.subpackage_length]
                    if not data.strip("0"):
                        break
                    p = Packet(data)
                    p.parse()
                    self.subpackages.append(p)
                    self.position += p.package_end
                    i += p.package_end

        self.package_end = self.position

        self.data = self.data[:self.package_end]
        
    def package_tree(self, indent=0):
        d = self.__dict__.copy()
        sub = d.pop('subpackages')
        print(" "*indent + str(d))
        for p in sub:
            p.package_tree(indent + 2)
            
    def valid(self):
        return bool(
            self.version != -1
            and self.type != -1
            and (self.type != 4 or self.value != "")
            and (self.type == 4 or self.subpackages)
        )
        
    @classmethod
    def decode(cls, bpackage: str):
        return Packet(bpackage)
            

def solve(data: List[str]):
    hpackage = data[0].lower()
    bpackage = "".join(HEX_TO_BIN[l] for l in hpackage)
    p = Packet.decode(bpackage)
    p.parse()
    p.package_tree()
    return p.result
    
    
def main(filename: str):
    with open(filename, 'r') as f:
        print(solve(f.read().splitlines()))
    

if __name__ == '__main__':
    main("d16/input.txt")
    # main("d16/example.txt")