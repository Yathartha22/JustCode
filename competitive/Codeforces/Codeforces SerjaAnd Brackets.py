from math import ceil, log2, sqrt

def constructST(s, start, end, st, i):
	if start == end:
		st[i] = 0
		openst[i] = 1 if s[start] == '(' else 0
		closedst[i] = 1 if s[start] == ')' else 0
		return st[i], openst[i], closedst[i]

	else:
		mid = (start+end)//2
		st[i], openst[i], closedst[i] = constructST(s, start, mid, st, 2*i+1) 
		a, b, c = constructST(s, mid+1, end,  st, 2*i+2)
		tmp = min(openst[2*i+1], closedst[2*i+2])
		st[i] += tmp + a
		openst[i] += b-tmp
		closedst[i] += c -tmp

		return st[i], openst[i], closedst[i]

def query(s, start, end, l, r, st, i):
	if l > end or r < start:
		return 0, 0, 0
	elif start >= l and end <= r:
		return st[i], openst[i], closedst[i]
	else:
		mid = (start + end)//2
		a, b, c = query(s, start, mid, l, r, st, 2*i+1) 
		d, e, f = query(s, mid+1, end, l, r, st, 2*i+2)
		tmp = min(b, f)
		T = a+d +tmp
		O = b+e - tmp
		C = c+f - tmp
	return T, O, C



s = input()
n = len(s)
x = int(ceil(log2(n)))
max_size = 2*pow(2, x) -1	

st = [0 for i in range(0, max_size)]
openst = [0 for i in range(0, max_size)]
closedst = [0 for i in range(0, max_size)]

constructST(s, 0, n-1, st, 0)
# print(st)
# print(openst)
# print(closedst)
for _ in range(int(input())):
	l, r = map(int, input().split())
	print(2*query(s, 0, n-1, l-1, r-1, st, 0)[0])
