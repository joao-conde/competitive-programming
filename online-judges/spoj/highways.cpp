//https://www.spoj.com/problems/HIGHWAYS/

#include <bits/stdc++.h>
using namespace std;

#define INF 1000000000 //high value simmulating infinity

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

    int testCases;
    cin >> testCases;
    while(testCases--){

        int cities, highways, src, dest;
        cin >> cities >> highways >> src >> dest;

        vector< vector<edge> > g(cities);
        vector<int> dist(g.size(), INF);
        vector<int> prev(g.size(), INF);

        for(int i = 0; i < highways; i++){
            int src, dst, cost;
            cin >> src >> dst >> cost;
            g[src-1].push_back({dst-1, cost});
            g[dst-1].push_back({src-1, cost});
        }

        int distance = dijkstra(g, src-1, dest-1, dist, prev);

        cout << (distance != INF ? to_string(distance) : "NONE") << "\n";

    }
}
