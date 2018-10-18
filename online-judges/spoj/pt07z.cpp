//http://www.spoj.com/problems/PT07Z/

#include <bits/stdc++.h> //Includes ALL c++ files needed

using namespace std;

#define INF 1000000000 //high value simmulating infinity

/* TIL:
*   1 - bfs calculates all shortest distances from a node
*   2 - graph can have bi-directional edges
*   3 - to find the middle of a tree, find the maximum distance from the source, then find
*   the maximum distance from that furthest node 
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

    ios::sync_with_stdio(0); //Input and output become more efficient.
    cin.tie();

    int computers, src, dest, treeDiam;

    cin >> computers;
        
    int maxIdx = -1, max = -1;
    vector<vector<int>> network(computers);
    vector<int> dist(network.size(), INF), dist2(network.size(), INF);

    //build network from user input
    for(int j = 0; j < computers - 1; j++){
        cin >> src; cin >> dest;

        //bi-directional edges so bfs calculates
        network[src-1].push_back(dest-1);
        network[dest-1].push_back(src-1);
    }

    //use bfs to calculate distances from first node and discover furthest node from root
    bfs(network, 0, dist); 
    for(int k = 0; k < dist.size(); k++){
        if(dist[k] > max){
            max = dist[k];
            maxIdx = k;
        }      
    }
        
    //use bfs to calculate biggest distance for furthest node = tree diameter
    bfs(network, maxIdx, dist2);
    treeDiam = *max_element(dist2.begin(),dist2.end());

    cout << treeDiam << endl;
    
    return 0;
}
