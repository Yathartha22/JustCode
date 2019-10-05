/* ShellSort is mainly a variation of Insertion Sort. In insertion sort, we move elements only one position ahead. 
When an element has to be moved far ahead, many movements are involved. The idea of shellSort is to allow exchange of far items. 
In shellSort, we make the array h-sorted for a large value of h. We keep reducing the value of h until it becomes 1. 
An array is said to be h-sorted if all sublists of every h’th element is sorted. */
#include<iostream>
using namespace std;
void shellSort(int *arr, int n){
    for (int gap = n/2; gap > 0; gap /= 2){
        for (int i = gap; i < n; i += 1){
            int temp = arr[i];
            int j;             
            for (j = i; j >= gap && arr[j - gap] > temp; j -= gap)
                arr[j] = arr[j - gap];
            arr[j] = temp; 
        }
    }
}
int main() 
{ 
    int *arr, n, i;
    cin>>n;
    arr=new int[n];
    for(i=0;i<n;i++){
    	cin>>arr[i];
	}
    shellSort(arr, n);
  	for (int i=0; i<n; i++)
        cout << arr[i] << " ";
    return 0;
}
