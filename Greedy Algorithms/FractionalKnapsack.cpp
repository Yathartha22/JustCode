#include <bits/stdc++.h>

using namespace std;

bool mySort(vector<long long> a, vector<long long> b){
	
	if (a[0] == b[0]) {
		if (a[2] == b[2]) {
			return (a[1] < b[1]);
		}
		return (a[2] > b[2]);
	}
	return (a[0] < b[0]);
}

long long go(vector<vector<long long>> worker, long long area){
	long long n = worker.size();
	sort(worker.begin(),worker.end(),mySort);

	long long cost = worker.at(0)[1];
	long long area_done = 0;
	long long current_worker = 0;
	long long last = 0;

	for (int i = 1; i < n && area_done<area; ++i)
	{
		last = i-1;
		long long time_gap = worker.at(i)[0]-worker.at(last)[0];

		// cout << "Worker: "<<current_worker << '\n';
		// cout << "Timegap: "<<time_gap << '\n';
		
		area_done += time_gap*(worker.at(current_worker)[2]);

		// cout <<"Cost: "<<cost<< '\n';
		// cout <<"Area done: "<<area_done<< '\n'<<endl;

		
		if (area_done>=area)
		{
		
			return cost;
 			
		}

		if (worker.at(current_worker)[2]<worker.at(i)[2])
		{
			current_worker = i;
			cost += worker.at(current_worker)[1];
		}
		
	}


	return cost;



}


int main( int argc , char ** argv )
{
	ios_base::sync_with_stdio(false) ; 
	cin.tie(NULL) ; 
	
	long long n;
	long long d;
	cin>>n>>d;
	vector<vector<long long>> worker;

	while(n--){
		long long t,x,y;
		cin>>t>>x>>y;

		vector<long long> temp;
		temp.push_back(t);
		temp.push_back(x);
		temp.push_back(y);

		worker.push_back(temp);
	}

	cout << go(worker, d) << '\n';



	return 0 ; 



}
