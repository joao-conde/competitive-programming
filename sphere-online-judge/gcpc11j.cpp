//http://www.spoj.com/problems/GCPC11J/

#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;


#define MAX 100000 //10⁵ which is max number of nodes, so edges is that -1 (roughly the same)
#define INF 1000000000 //high value simmulating infinity


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

    ios::sync_with_stdio(0); // Input and output become more efficient.
    cin.tie();

    int test_cases, computers, src, dest, furthestNode, treeDiam;
    cin >> test_cases;

    for(int i = 0; i < test_cases; i++){
        
        cin >> computers;
        
        vector<vector<int>> network(computers);
        vector<int> dist(network.size(), INF), dist2(network.size(), INF);

        //build network from user input
        for(int j = 0; j < computers - 1; j++){
            cin >> src; cin >> dest;

            //bi-directional edges
            network[src].push_back(dest);
            network[dest].push_back(src);
        }


        //use bfs to calculate distances from first node and discover furthest node from root
        bfs(network, 0, dist); 
        furthestNode = *max_element(dist.begin(), dist.end());



        bfs(network, furthestNode, dist2);
        treeDiam = *max_element(dist2.begin(),dist2.end());


        cout << "FURTHESTNODE " << furthestNode << " treeDiam " << treeDiam << endl;
        cout << treeDiam / 2 + treeDiam % 2 << endl;
    }
    
    return 0;
}
