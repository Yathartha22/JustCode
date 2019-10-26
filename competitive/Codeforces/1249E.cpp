/*****************************************************

@author: Knife_PParty
Compiled On: 23st Oct 2019

*****************************************************/

#include<iostream>
using namespace std;
int n,c,a[200001],b[200001];
long long f[200001][2];
int main()
{
	cin>>n>>c;
	for (int i=1;i<n;i++) cin>>a[i];
	for (int i=1;i<n;i++) cin>>b[i];
	f[1][0]=0; f[1][1]=c;
	cout<<0<<" ";
	for (int i=2;i<=n;i++)
	{
		f[i][0]=min(f[i-1][0]+a[i-1],f[i-1][1]+a[i-1]);
		f[i][1]=min(f[i-1][0]+c+b[i-1],f[i-1][1]+b[i-1]);
		cout<<min(f[i][0],f[i][1])<<" ";
	}
}
