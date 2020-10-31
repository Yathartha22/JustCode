#code
counting inversion-of-array using mergesort

link: https://practice.geeksforgeeks.org/problems/inversion-of-array/0


def mergeSort(a, start, end, temp):
    inv_count = 0
    
    mid = (start+end)//2
    
    if start < end:
        inv_count += mergeSort(a, start, mid, temp)
        inv_count += mergeSort(a, mid+1, end, temp)
        
        inv_count += merge(a, start, mid, end, temp)
    
    return inv_count

def merge(a, start, mid, end, temp):
    i = start
    j = mid+1
    k = start
    inv_count = 0
    
    while i <= mid and j <= end:
        if a[i] <= a[j]:
            temp[k] = a[i]
            i += 1
            k += 1
        else:
            temp[k] = a[j]
            inv_count += (mid-i +1)
            j+= 1
            k+=1
    
    while i <= mid:
        temp[k] = a[i]
        i+=1
        k+=1
    
    while j <= end:
        temp[k] = a[j]
        j+=1
        k+=1
    
    for i in range(start, end+1):
        a[i] = temp[i]
    
    return inv_count
        
    
for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    
    temp = [0 for i in range(n)]
    print(mergeSort(a, 0, n-1, temp))
    
    