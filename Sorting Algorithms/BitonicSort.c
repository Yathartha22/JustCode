#include<stdio.h>  
void exchange(int arr[], int i, int j, int d)  
{  
    int temp;  
    if (d==(arr[i]>arr[j]))  
    {  
            temp = arr[i];  
        arr[i] = arr[j];  
        arr[j] = temp;  
    }  
}  
void merge(int arr[], int l, int c, int d)  
{  
    int k,i;  
    if (c>1)  
    {  
        k = c/2;  
        for (i=l; i<l+k; i++)  
            exchange(arr, i, i+k, d);  
        merge(arr, l, k, d);  
        merge(arr, l+k, k, d);  
    }  
}  
void bitonicSort(int arr[],int l, int c, int d)  
{  
    int k;  
    if (c>1)  
    {  
        k = c/2;  
        bitonicSort(arr, l, k, 1);  
        bitonicSort(arr, l+k, k, 0);  
        merge(arr,l, c, d);  
    }  
}  
   
void sort(int arr[], int n, int order)  
{  
    bitonicSort(arr,0, n, order);  
}  
int main()  
{  
    int arr[100],n,i,order = 1;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
    	scanf("%d",&arr[i]);
    }     
    sort(arr, n, order);  
   
    printf("Sorted array: \n");  
    for (i=0; i<n; i++)  
        printf("%d ", arr[i]);  
}
