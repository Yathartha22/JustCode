title: longest common prefix in an array
source: https://practice.geeksforgeeks.org/problems/longest-common-prefix-in-an-array/0
tags: strings

# code
def prefix(s1, s2):
    n = len(s1)
    m = len(s2)
    i = 0
    while i < m and i < n:
        if s1[i] != s2[i]:
            break
        i+=1
    if i == 0:
        return 0
    else:
        return i
        
for t in range(int(input())):
    l = int(input())
    s = [i for i in input().split()]

    f = 1
    if l>1:
        for i in range(0, l-1):
            p = prefix(s[i], s[i+1])
            if p == 0:
                f = 0
                break
            else:
                if i == 0:
                    max_len = p
                else:
                    max_len = min(p, max_len)
    
    if l == 1:
        print(s[0])
    elif f:
        print(s[0][:max_len])
    else:
        print(-1)
