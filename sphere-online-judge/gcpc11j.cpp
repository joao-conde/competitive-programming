//http://www.spoj.com/problems/GCPC11J/

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>


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

    int test_cases, computers, src, dest;
    cin >> test_cases;

    for(int i = 0; i < test_cases; i++){
        
        cin >> computers;
        vector< vector<int> > network(computers);
        

        //build network from user input
        for(int j = 0; j < computers - 1; j++){
            cin >> src; cin >> dest;
            network[src].push_back(dest);
            network[dest].push_back(src);
        }

        
        int networkTTL = INF;
          
        
        //calculate maximum ttl assuming a router, choose the router assumption with smaller TTL
        for(int l = 0; l < computers; l++){
            vector<int> dist(network.size(), INF);
            bfs(network, l, dist); 

            if(networkTTL > *max_element(dist.begin(), dist.end()))
                networkTTL = *max_element(dist.begin(), dist.end());

            cout << "---ROUTER ON " << l << "---" << endl; 
            for(int distancia: dist){
                cout << "DIST: " << distancia << endl;
            }
            
        }
        
        cout << "TEST CASE " << i+1 << ": " << networkTTL << endl;
      
    }
    
    return 0;
}
