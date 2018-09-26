//https://www.spoj.com/problems/SAMER08A/

#include <bits/stdc++.h>
using namespace std;


#define INF 1000000000

struct edge{ 
    int to, cost; 
};

int dijkstra(vector< vector<edge> > &g, int source, int target, vector<int>& dist, vector<int>& prev){

    dist[source] = 0;
    prev[source] = -1;
    set< pair<int, int> > active;
    active.insert( {0, source} );

    while (!active.empty()) {
        int cur = active.begin()->second;
        if (cur == target) return dist[cur];
        active.erase( active.begin() );

        for (edge ed : g[cur]){
            if (dist[ed.to] > dist[cur] + ed.cost) {
                active.erase( { dist[ed.to], ed.to } );
                dist[ed.to] = dist[cur] + ed.cost;
                prev[ed.to] = cur;
                cout << "EDGE: " << ed.to << " --- " << ed.cost << endl;
                active.insert( { dist[ed.to], ed.to } );
            }
        } 
    }
    return INF;
}

int main() {

    ios::sync_with_stdio(0); 
    cin.tie();

    while(true){

        int nodes, edges; 
        cin >> nodes >> edges;
        
        if(nodes == 0 && edges == 0) break;
        
        vector< vector<edge> > g(nodes);
        
        int s0, sf; 
        cin >> s0 >> sf;
        for(int i = 0; i < edges; i++){
            int src, dest, cost; 
            cin >> src >> dest >> cost;
            g[src].push_back( {dest, cost} );
        }

        vector<int> dist(nodes, INF), prev(nodes, INF);

        dijkstra(g, s0, sf, dist, prev);

        for(int i = 0; i < prev.size(); i++){
            
        }
        
        fill(dist.begin(), dist.end(), INF);
        fill(prev.begin(), prev.end(), INF);
        
        cout << dijkstra(g, s0, sf, dist, prev) << endl; 


    }

}
