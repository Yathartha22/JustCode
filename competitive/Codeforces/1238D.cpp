/*****************************************************

@author: vichitr
Compiled On: 1st Oct 2019

*****************************************************/
#include<bits/stdc++.h>
#define MAX 9223372036854775807
#define endl "\n"
#define ll long long
#define int long long
#define double long double
#define pb push_back
#define pf pop_front
#define mp make_pair
#define ip pair<int, int>

#define loop(i,n) for(int i=0;i<n;i++)
#define loops(i,s,n) for(int i=s;i<=n;i++)
#define fast ios::sync_with_stdio(0); cin.tie(NULL); cout.tie(NULL)
using namespace std;

const ll MOD = 1e9+7;
const ll SZ = 320;
const ll N = 3e5+1;
const ll M = 2e5+7;

ll pwr(ll x, ll y)
{
    ll r = 1LL;
    while(y)
    {
        if(y&1)
            r = (r * x) % MOD;
        y >>= 1;
        x = (x * x) % MOD;
    }
    return r;
}

int inv(int x)
{
	return pwr(x, MOD-2ll);
}

int cnt[500][26];

void solve()
{
	int  n; string s; cin>>n>>s;
	int ans = 0;
	vector<int> v; int k = 1, c=s[0];
	ans = n*(n+1)/2 - n;
	for(int i=1;i<n;i++)
	{
		if(s[i]==c)
			k++;
		else{
			v.pb(k);
			k = 1;
			c = s[i];;
		}
	}
	v.pb(k);
	for(int i=1;i<v.size();i++)
		ans -= v[i];
	for(int i=0;i<v.size()-1;i++)
		ans -= (v[i]-1);
	cout<<ans;
}

signed main()
{
    fast;
    int t=1;
    // cin >>t;
    while(t--){
        solve();
        
    }
    return 0;
}

/*****************************

5 4
1 2
4 3
1 4
3 4

1

6 5
2 3
2 1
3 4
6 5
4 5

0

****************************/
