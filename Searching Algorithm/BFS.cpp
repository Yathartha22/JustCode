
		//Breadth_first_search for undirected and unweighted graph

#include<iostream>
#include<vector>
#include<queue>
#include<stack>
#include<map>
#define rep(i,a,b) for(int i=a;i<b;i++)
#define pb push_back
using namespace std ;
map<char,vector<char>> edges;

void Bfs(char root)
{
	cout << "\nBreadth_first_search : " ;
	queue <char> visitRank ;
	map <char,bool> visited ;

	char currNode = root ;
	visitRank.push(currNode);
	visited[currNode]=true;
	while(!visitRank.empty())
	{
		currNode = visitRank.front();
		for(auto c : edges[currNode])
			if(!visited[c])
				visitRank.push(c),visited[c]=true;
		cout << currNode << " ";
		visitRank.pop();
	}
}


void Dfs(char root)
{
	cout << "\nDepth_irst_search : " ;
	stack <char> visitRank;
	map <char,bool> visited ;
	char currNode = root ;
	visitRank.push(currNode);
	visited[currNode]=true;
	while(!visitRank.empty())
	{
		cout << currNode << " ";
		currNode = visitRank.top();
		for(auto c : edges[currNode])
			if(!visited[c])
				visitRank.push(c),visited[c]=true,currNode=c;
		visitRank.pop();
	}
}

int main()
{
	int totalNodes,totalEdges ;

	cout << "Enter Total Nodes : " ;
	cin >> totalNodes ;
	cout << "Enter total number of Edges : ";
	cin >> totalEdges ;


	char u,v ;

	rep(i,0,totalEdges)
	{
		cin >> u >> v ;
		edges[u].pb(v);
		edges[v].pb(u);
	}
	char root ;
	cout << "Enter Root : " ;
	cin >> root ;
	while(edges[root].size()==0)
	{
		cout << "Not Valid Root Node, " << "Enter Again : " ;
		cin >> root ;
	}
	Bfs(root);
	Dfs(root);
}

