#include <iostream>
#include<cmath>
#include<cstring>
using namespace std;
int j;
int a[10000000];
int rec(int n,int temp)
{
    if(n==1)
    return(1);
    else
    {  while(j<temp){
        int r=pow(2,j+1);
        for(int i=pow(2,j)-1;i<n;i+=r)
        {
            a[i]=-1;
        }
        j++;
        
    }
    int i;
    
    if(temp==j)
    for(i=0;i<n;i++)
    if(a[i]==0){
    break;}
    return(i+1);
    }
}
int main() {
	int t;
	cin>>t;
	while(t--)
	{ j=0;
	    int n;
	    int i;
	    cin>>n;
	    memset(a,0,sizeof(a));
	    for(i=1;i<10000;i++)
	    if(n<pow(2,i))
	    break;
	    
	    cout<<rec(n,i-1)<<endl;
	}
	return 0;
}
