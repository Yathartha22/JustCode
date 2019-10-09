# Python program for implementation of Bogo Sort 
import random 

# Sorts array a[0..n-1] using Bogo sort 
def bogoSort(array): 
	n = len(array) 
	while (is_sorted(array)== False): 
		shuffle(array) 

# To check if array is sorted or not 
def is_sorted(array): 
	n = len(array) 
	for i in range(0, n-1): 
		if (array[i] > array[i+1] ): 
			return False
	return True

# To generate permuatation of the array 
def shuffle(array): 
	n = len(array) 
	for i in range (0,n): 
		r = random.randint(0,n-1) 
		array[i], array[r] = array[r], array[i] 

# Driver code to test above 
array = [3, 2, 4, 1, 0, 5] 
bogoSort(array) 
print("Sorted array :") 
for i in range(len(array)): 
	print("{0}".format(array[i]))
