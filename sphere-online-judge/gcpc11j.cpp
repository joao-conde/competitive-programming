//http://www.spoj.com/problems/GCPC11J/

#include <iostream>
#include <vector>
#include <queue>


using namespace std;


#define MAX 100000 //10⁵ which is max number of nodes, so edges is that -1 (roughly the same)
#define INF 1000000000 //high value simmulating infinity

/*
*   Since every edge of an elGraph is basically a pair<int,pair<int,int>>:
*       - COST is given by pair.first
*       - SRC is given by pair.second.first
*       - DEST is given by pair.second.second
*/


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


int main(){

    int test_cases, ttl, computers, src, dest;
    cin >> test_cases;

    for(int i = 0; i < test_cases; i++){
        ttl = -1;
        cin >> computers;
        //use belman ford, get maximum value, that = TTL, that node is router, if next iter has smaller ttl, thats the router
        //do untill no more nodes, print TTL

        vector< vector<int> > network(computers);

        for(int j = 0; j < computers - 1; j++){
            cin >> src; cin >> dest;
            network[src].push_back(dest);
        }

        vector<int> dist(network.size(), INF);
        
        for(int l = 0; l < computers; l++){
            bfs(network, l, dist); 
            if(dist[l] > ttl) ttl = dist[l];
        }
        
        cout << "TEST CASE " << i+1 << ": " << ttl << endl;
      
    }
    
    return 0;
}