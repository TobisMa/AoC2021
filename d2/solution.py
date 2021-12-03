class Submarine:
    def __init__(self, x, depth):
        self.x = x
        self.depth = depth
        self.aim = 0
    
    def __repr__(self):
        return "Submarine(x=%s, depth=%s)" % (self.x, self.depth)
        
    def navigation(self, commands):
        for command in commands:
            split_command = command.split(" ")
            if split_command[0] == "forward":
                self.x += int(split_command[1])
                self.depth += self.aim * int(split_command[1]) # 2nd
            
            elif split_command[0] == "down":
                self.aim += int(split_command[1])   #...aim = 2nd
            
            elif split_command[0] == "up":
                self.aim -= int(split_command[1])   # ...aim = 2nd
        

if __name__ == "__main__":
    submarine = Submarine(0, 0)
    with open("a2/input.txt", "r") as f:
        submarine.navigation(f.read().splitlines())
    print(submarine)