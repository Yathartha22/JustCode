# title: coin change problem
# source: https://practice.geeksforgeeks.org/problems/coin-change/0
# tags: dynamic programming

# code
for t in range(int(input())):
    m = int(input())
    a = [int(i) for i in input().split()]
    n = int(input())
    
    dp = [[-1 for i in range(0, m)] for j in range(0, n+1)]

    for i in range(m):
        dp[0][i] = 1

    for i in range(1, n+1):
        for j in range(0, m):
            x, y = 0, 0
            if i-a[j] >= 0:
                x = dp[i-a[j]][j]
            if j >= 1:
                y = dp[i][j-1]
            dp[i][j] = x + y
            
    print(max(dp[n][m-1], 0))
