#code
# counting inversion-of-array using mergesort

# link: https://practice.geeksforgeeks.org/problems/inversion-of-array/0


def update(Bitree, i, n, val):
    while i < n:
        print(i)
        Bitree[i] += val
        i += i&(-i)
    


def getSum(Bitree, i, n):
    sum = 0
    
    while i > 0:
        sum += Bitree[i]
        
        i -= i&(-i)
    return sum


def constructBit(Bitree, a2, n):
    inv_count = 0
    for i in range(n-1, -1, -1):
        inv_count += getSum(Bitree, a2[i], n)
        update(Bitree, a2[i]+1, n, 1)
    return inv_count



for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    
    Bitree = [0 for i in range(0, n+1)]
    
    temp = sorted(a)
    a2 = [0 for i in range(0, n)]
    d = {temp[i] :i  for i in range(0, n)}
    for i in range(0, n):
        a2[i] = d[a[i]]
    
    # print(a2)
    print(constructBit(Bitree, a2, n))
    
    
     