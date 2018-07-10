//src: https://www.geeksforgeeks.org/fast-io-for-competitive-programming/

#include <bits/stdc++.h>
using namespace std;

/* TIL:
*   1 - ...
*   2 - ...
*   3 - ...
*/


#define INF 1000000000

void bfs(const vector< vector<int> > &g, int source, vector<int>& dist) {
	queue<int> q;
	dist[source] = 0;
	q.push(source);

	while (!q.empty()) {
		int cur = q.front(); q.pop();
		for (int e : g[cur]) 
			if (dist[e] == INF) {
				dist[e] = dist[cur] + 1;
				q.push(e);
			}
	}
}


vector<vector<int>> buildGraph(vector<pair<int,int>> edges, int size){

	vector<vector<int>> graph(size);

	for(int i = 0; i < edges.size(); i++){
		graph[edges[i].first].push_back(edges[i].second);
	}

	return graph;
}

int main() {
    ios::sync_with_stdio(0); 
    cin.tie();

    int src, dest;    
    while(true){

    	cin >> src; cin >> dest;

    	if(src == 0 && dest == 0) break;

    	int size = max(src,dest);
    	vector<pair<int,int>> edges;
    	edges.push_back(make_pair(src,dest));

    	while(true){
    		cin >> src; cin >> dest;

    		if(src == 0 && dest == 0) break;

    		edges.push_back(make_pair(src,dest));
    		size = max(size, max(src,dest));
    	}

    	cout << "HERE\n";

    	size -= 1;
    	vector<vector<int>> graph = buildGraph(edges, size);

    	int sum = 0, combinations = 0;

		for(int i = 0; i < size; i++){
			vector<int> dist(size, INF);
			bfs(graph, i, dist);

			for(int j = 0; j < dist.size(); j++){
				sum += dist[j];
				combinations++;
			}
		}

    	//print testcase results
    	cout << "AVG: " << (double)sum / double(combinations) << "\n";
    }


}

