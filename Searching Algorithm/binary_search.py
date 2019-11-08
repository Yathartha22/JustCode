#Binary sort with Recursive way
#it is used to find the sortest list element by recursion

def binarySearch (arr, l, r, x): 
    if r >= l: 
  
        mid = l + (r - l)/2
  
        
        if arr[mid] == x: 
            return mid 
          
      
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
  
        
        else: 
            return binarySearch(arr, mid+1, r, x) 
  
    else: 
       
        return -1
        
        
#for only test purpose

arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  

result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index",result) 
else: 
    print("Element is not present in array")
