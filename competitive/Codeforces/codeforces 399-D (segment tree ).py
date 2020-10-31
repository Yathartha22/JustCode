#codeforces contest 339 problem D
# link: https://codeforces.com/contest/339/problem/D
from sys import stdin, stdout

from math import log2, ceil, floor
def construct(a, start, end, stree, si, xor):
    if start == end:
        stree[si] = a[start]
        return stree[si]
    mid = (start+end)//2
    if xor:
        stree[si] = construct(a, start, mid, stree, 2*si+1, 0) ^ construct(a, mid+1, end, stree, 2*si+2, 0)
    else:
        stree[si] = construct(a, start, mid, stree, 2*si+1, 1) | construct(a, mid+1, end, stree, 2*si+2, 1)
    return stree[si]

def getv(a, start, end, l, r, stree, si):
    return stree[0]

def update(a, start, end, i, val, stree, si, xor):
    if i > end or i< start:
        return 0
    if start == end:
        a[i] = val
        # print(si)
        stree[si] = val
        return

    mid = (start+end)//2
    if i >= start and i <=mid:
        update(a, start, mid, i, val, stree, 2*si+1, 1-xor)
    else:
        update(a, mid+1, end, i, val, stree, 2*si+2, 1-xor)

    if xor:
        # print(si)
        stree[si] = stree[2*si +1] ^ stree[2*si + 2]
        # xor = 0
        # print(stree[si])
    else:
        stree[si] = stree[2*si +1] | stree[2*si + 2]
        # xor = 1



n, m = map(int, stdin.readline().split())
a = [int(i) for i in stdin.readline().split()]
x= int(ceil(log2(n)))
size = pow(2, n)

max_height= 2*pow(2, n) -1

stree = [0 for i in range(max_height)]
xor = 1 if n%2 == 0 else 0
construct(a, 0, size-1, stree, 0, xor)
# print(stree)
# xor  = 0
for i in range(0, m):
    p, val = map(int, stdin.readline().split())
    update(a, 0, size-1, p-1, val, stree, 0, xor)
    stdout.write(str(stree[0]))
    stdout.write("\n")


