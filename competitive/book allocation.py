import sys

A = [int(i) for i in input().split()]
B = int(input())
# n = len(a)

# psum = [0 for i in range(0, n)]
# psum[0] = a[0]
# for i in range(1, n):
#     psum[i] = psum[i-1] + a[i]

 
# def sol(a, b, n, psum, dp):
#     if b ==1 or n== 1:
#         return psum[n-1]
#     else:
#         res = sys.maxsize
#         for i in range(n-1, 0, -1):
#             # print(res)
#             if not dp[i][b-1]:
#                 dp[i][b-1] = sol(a, b-1, i , psum, dp)
#             res = min(res, max(psum[n-1] - psum[i-1], dp[i][b-1]))
#     return res
# # if n == m
# dp = [[0 for i in range(0, b+1)] for j in range(0, n)]
# print(sol(a, b, len(a), psum, dp))                            


end = sum(A)
start = max(A)
n = len(A)
while start < end:
    max_pages = start+ (end-start)//2
    pages = 0
    count = 1
    # print(start , end, max_pages)
    for i in range(n):
        if pages + A[i] <= max_pages:
            pages+= A[i]
        else:
            count += 1
            pages = A[i]
    if count > B:
        start = max_pages +1
    else:
        end = max_pages
print(start)
