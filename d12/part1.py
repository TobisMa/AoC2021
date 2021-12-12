from typing import Generator, Iterable, List, Optional, Set, Tuple


class Cave:
    
    start = None
    end = None
    caves = {}
    
    def __new__(cls, name, *neighbors):
        c = Cave.caves.get(name)
        if c is not None:
            return c
        return super().__new__(cls)
    
    def __init__(self, name: str, *neighbors) -> None:
        Cave.caves[name] = self
        self.name = name
        self.neighbors: Set[str] = set(neighbors)
        self.small = name.islower()
    
    def __repr__(self):
        return "Cave(%r, neighbors=%s)" % (self.name, self.neighbors)
    
    def __iter__(self):
        yield from [Cave.caves[c] for c in self.neighbors]
    
    def __next__(self):
        yield from self.__iter__()
    
    def add_neighbor(self, neighbor: str):
        self.neighbors.add(neighbor)


class Routing(object):
    def __init__(self, *caves: Cave):
        self.caves = caves
        self.paths: Set[Tuple[Cave, ...]] = set()
        
    def find_all_paths(self):
        start: Optional[Cave] = Cave.start
        if start is None:
            return "No starting point"

        self.find_next([start])
        
    def find_next(self, path: List[Cave]):
        c: Cave
        cave = path[-1]
        for c in cave:
            if c.name == Cave.end.name:
                self.paths.add(tuple(path + [c]))

            elif c.small and c not in path or not c.small:
                self.find_next(path=path + [c])
                

    @classmethod
    def create_navigation(cls, lines: List[str]):
        Cave.start = Cave("start")
        Cave.end = Cave("end")
        
        caves = {
            "start": Cave.start,
            "end": Cave.end
        }
        for line in lines:
            start, end = line.split("-")
            
            if caves.get(start) is None:
                caves[start] = Cave(start)
            caves[start].add_neighbor(end)
            
            if caves.get(end) is None:
                caves[end] = Cave(end)
            caves[end].add_neighbor(start)
            
        return cls(*caves.values())


def main(filename):
    with open(filename, 'r') as f:
        r = Routing.create_navigation(f.read().splitlines())
    r.find_all_paths()
    # print([[e.name for e in x] for x in r.paths])
    print(len(r.paths))
    

if __name__ == '__main__':
    # main("d12/example.txt")
    main("d12/input.txt")