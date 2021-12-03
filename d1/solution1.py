def check(v):
	v = [int(x) for x in v if x]
	return sum(v[i-1] < v[i] for i in range(1, len(v)))


if __name__ == '__main__':
    with open("d1/input.txt", "r") as f:
        contents = f.read()
        
    print(check(contents.splitlines()))