# title: Buy sell stock
# source: https://practice.geeksforgeeks.org/problems/stock-buy-and-sell/0
# tags: arrays

# code
import sys
for t in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    
    buy = 0
    profit = 0
    a = [sys.maxsize] + a + [-1]
    d = []
    
    for i in range(0, n+1):
        if not buy:
            if a[i-1] > a[i] and a[i+1] > a[i]:
                buy = 1
                b = str(i-1)
                profit -= a[i]
        else:
            if a[i-1] < a[i] and a[i+1] <  a[i]:
                buy = 0
                p = "("+b+" "+str(i-1)+")"
                d.append(p)
                profit += a[i]
    
    if profit <= 0:
        print("No Profit")
    else:
        print(*d)
