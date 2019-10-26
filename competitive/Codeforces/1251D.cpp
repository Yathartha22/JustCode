/*****************************************************

@author: Knife_PParty
Compiled On: 25st Oct 2019

*****************************************************/
#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int,int> ii;

bool ok(ll mid, const vector<ii> &v, ll s, int n) {
	ll ret=0;
	int m=(n+1)/2;
	for (int i=0; i<n; i++)
		if (v[i].second>=mid&&m) ret+=max(mid,ll(v[i].first)), m--;
		else ret+=v[i].first;
	return !m&&ret<=s;
}

int main() {
	cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);
	int t; cin>>t;
	while(t--) {
		int n; ll s; cin>>n>>s;
		vector<ii> v(n);
		for (int i=0; i<n; i++)
			cin>>v[i].first>>v[i].second;
		sort(v.rbegin(),v.rend());
		ll low=0, high=s, mid;
		while(low<high) {
			mid=(low+high+1)/2;
			if(ok(mid,v,s,n)) low=mid;
			else high=mid-1;
		}
		cout<<low<<endl;
	}
	return 0;
}

