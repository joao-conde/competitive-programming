//https://www.spoj.com/problems/TRSTAGE/

#include <bits/stdc++.h>
using namespace std;

/* TIL:
*   1 - ...
*   2 - ...
*   3 - ...
*/

#define INF 1000000000 //high value simmulating infinity

int tickets[30];

struct edge { int to, cost; };

int dijkstra(vector< vector<edge> > &g, int source, int target, vector<int>& dist, vector<int>& prev) {
    dist[source] = 0;
    prev[source] = -1;
    set< pair<int, int> > active;
    active.insert( {0, source} );

    while (!active.empty()) {
        int cur = active.begin()->second;
        
        if (cur == target) return dist[cur];
        
        active.erase( active.begin() );
        for (edge ed : g[cur]) 
            if (dist[ed.to] > dist[cur] + ed.cost) {
                active.erase( { dist[ed.to], ed.to } );
                dist[ed.to] = dist[cur] + ed.cost;
                prev[ed.to] = cur;
                active.insert( { dist[ed.to], ed.to } );
            }
    }
    return INF;
}

int main() {
    
    ios::sync_with_stdio(0); 
    cin.tie();

    while(true){

        int ntickets, cities, roads, start, target;
        cin >> ntickets >> cities >> roads >> start >> target;

        if(ntickets == cities == roads == start == target == 0) break; //end of input

        for(int i = 0; i < roads; i++) cin >> tickets[i];

        vector<int> dist(cities, INF), prev(cities, INF);
        vector< vector<edge> > network(cities);
        for(int i = 0; i < roads; i++){
            int x, y, z;
            cin >> x >> y >> z;
            network[x-1].push_back({y-1, z});
        }

       

    }



}