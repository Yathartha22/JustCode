#codeforces contest 61 Problen E
#link: https://codeforces.com/contest/61/problem/E

def getSum(BiTree, i, n):
    sum = 0
    while i > 0:
        sum += BiTree[i]
        i -= i & (-i)
    return sum
from sys import stdin, stdout

def update(BiTree, i, n, val):
    while i <n:
        BiTree[i] += val
        i += i & (-i)




def construct(a, BiTree, a2, a3, n):
    lcount = [0 for i in range(n)]
    for i in range(0, n):
        lcount[i] = getSum(BiTree, a3[i], n)
        update(BiTree, a3[i] + 1, n, 1) 

    rcount = [0 for i in range(n)]
    BiTree = [0 for i in range(0, n+1)]
    for i in range(n-1, -1, -1):
        rcount[i] = getSum(BiTree, a2[i], n)
        update(BiTree, a2[i] +1, n, 1)

    s = 0
    for i in range(0, n):
        s += rcount[i]*lcount[i]
    return s


n = int(stdin.readline())
a = [int(i) for i in stdin.readline().split()]

BiTree = [0 for i in range(0, n+1)]

temp = sorted(a)
temp2 = temp[::-1]

d = {temp[i]: i for i in range(0, n)}
a2 = [d[a[i]] for i in range(0, n)]

d2 = {temp2[i]: i for i in range(0, n)}
a3 = [d2[a[i]] for i in range(0, n)]

stdout.write(str(construct(a, BiTree, a2, a3, n)))
