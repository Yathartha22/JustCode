def merge(arr, temp, left, mid, right):
    i, j, k = left, mid, left
    inv_count = 0
    while i <= mid - 1 and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k+=1; i+=1
        else:
            temp[k] = arr[j]
            k+=1; j+=1
            inv_count += (mid - i)
    
    while i <= mid - 1:
        temp[k] = arr[i]
        k+=1; i+=1
    
    while j<= right:
        temp[k] = arr[j]
        k+=1;j+=1
    
    for i in range(left, right + 1):
        arr[i] = temp[i]
    
    return inv_count
    
def mergesort(arr, temp, left, right):
    inv_count = 0
    if left == right:
        return 0
    
    mid = (left + right)//2
    inv_count = mergesort(arr, temp, left, mid)
    inv_count+= mergesort(arr, temp, mid+1, right)
    
    inv_count += merge(arr, temp, left, mid+1, right)
    
    return inv_count

t = int(input())
while t > 0:
    n = int(input())
    temp = [0]*n
    arr = [int(i) for i in input().split()]
    print(mergesort(arr, temp, 0, n-1))
    t-=1