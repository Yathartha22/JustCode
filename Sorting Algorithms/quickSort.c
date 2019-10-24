#include <stdio.h>
#include <stdlib.h>

/**
*
*AUTHOR: VinayV9
*Description: QuickSort
*
*/

void quickSort(int *a, int start, int end);
int partition(int *a, int start, int end);
void swap(int *a, int i, int j);


int main(){
	int a[] = {2, 3, 1, 11, 2, 1, 1, 2, 432, 2, 1, 22};
	int n = sizeof(a)/sizeof(a[0]); 
	quickSort(a, 0, n-1);
	for(int i = 0; i < n; i++){
		printf("%d ", a[i]);
	}
	return 0;
}


void quickSort(int *a, int start, int end){
	if(start < end){
		int pivot = partition(a, start, end);
		quickSort(a, start, pivot-1);
		quickSort(a, pivot+1, end);
	}
}


int partition(int *a, int start, int end){
	int pivot = a[start];
    int left  = start+1;
	for(int right = left; right <= end; right++){
		if(a[right] < pivot){
			swap(a, left, right);
			left += 1;
		}
	}
	swap(a, left-1, start);
	return left-1;
}


void swap(int *a, int i, int j){
	int temp = a[i];
	a[i] = a[j];
	a[j] = temp;
}