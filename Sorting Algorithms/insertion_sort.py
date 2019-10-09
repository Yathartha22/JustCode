# Function definition for Insertion Sort
def insertion_sort(arr):
    n = len(arr)
    
    # Traversing through all the elements of the array
    # All the elements at index < i are present in sorted order
    for i in range(1, n):
        val = arr[i]
        
        # Move the elements of arr[0:i-1] one position ahead which are greater than val
        j = i-1
        while j>=0 and val<arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = val
        
def main():
    arr = [64, 34, 25, 12, 22, 11, 90]
    insertion_sort(arr)
    
    print("Sorted Array: ")
    print(*arr)
    
if __name__ == '__main__':
    main()
    
        
