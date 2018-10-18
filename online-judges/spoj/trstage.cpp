//https://www.spoj.com/problems/TRSTAGE/

#include <bits/stdc++.h>
using namespace std;

#define INF 1000000000 //high value simmulating infinity

int tickets[50], cityTickets[40];

struct edge { int to, cost; };
int dijkstra(vector< vector<edge> > &g, int source, int target, int availableTickets, vector<int>& dist) {
    
    dist = vector<int>(g.size());    
    dist[source] = 0;
    
    set< pair<int, int> > active;
    active.insert( {0, source} );

    while (!active.empty()) {
        int cur = active.begin()->second;
        
        if (cur == target) return dist[cur];
        
        active.erase( active.begin() );
        
        for (edge ed : g[cur]) 
            if (dist[ed.to] > dist[cur] + ed.cost && cityTickets[cur] - tickets[ed.to] >= 0) {

                availableTickets -= tickets[ed.to];
                active.erase( { dist[ed.to], ed.to } );
                dist[ed.to] = dist[cur] + ed.cost;
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

        if(ntickets == 0 && cities == 0 && roads == 0 && start == 0 && target == 0) break; //end of input

        for(int i = 0; i < roads; i++) cin >> tickets[i];

        vector<int> dist(cities, INF);
        vector< vector<edge> > network(cities);
        for(int i = 0; i < roads; i++){
            int x, y, z;
            cin >> x >> y >> z;
            network[x-1].push_back({y-1, z});
        }

        cityTickets[start] = ntickets;
        cout << dijkstra(network, start, target, ntickets, dist) << endl;


    }



}