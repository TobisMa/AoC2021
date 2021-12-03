def check(v):
	v = [int(x) for x in v if x]
	return sum(v[i-1] < v[i] for i in range(1, len(v)))