#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int f(int x,int y)
{
    if(x==y)
    return 0;
    else
    {
     int temp=x^y;
     int count=0;
     bitset<32>b1(temp);
     count=b1.count();
     
     return count;
    }
}
int main()
{
	int t;
	
	cin>>t;
	while(t--)
	{
	    int n;
	    long long int sum=0;
	    cin>>n;
	    int a[n];
	    for(int i=0;i<n;i++)
	    cin>>a[i];
	    for(int i=0;i<n;i++)
	    for(int j=0;j<n;j++)
	    {   
	       sum+=f(a[i],a[j]); 
	    }
	    cout<<sum<<endl;
	}
	return 0;
}
