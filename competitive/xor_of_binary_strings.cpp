    #include<bits/stdc++.h>
    using namespace std;
    int main(){
    int t;
    string a,b;
    cin>>t;
    while(t--){
        cin>>a>>b;
        string res="";
        for(int i=0;i<a.length();i++)
        {
            res+=to_string(int(a[i])^int(b[i]));
        }
        cout<<res;
        
    }
    return 0;
    }
