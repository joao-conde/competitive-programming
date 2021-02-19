//https://www.spoj.com/problems/MICEMAZE/

#include <bits/stdc++.h>
using namespace std;

/* TIL:
*   1 - Faster to make N dijkstra calls ( N * O(E + N*log(N)) ) for each of the N nodes rather than use Floyd ( O(N³) )
*/

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

    int cells, exitCell, timer, connections, mice = 0;
    cin >> cells >> exitCell >> timer >> connections;

    vector< vector<edge> > maze(cells);
    for(int i = 0; i < connections; i++){
        int src, dst, cost;
        cin >> src >> dst >> cost;
        maze[src-1].push_back({dst-1, cost});
    }

    //dijkstra for each node, if distance is smaller or equal to time it exits the maze
    for(int i = 0; i < cells; i++){
        vector<int> dist(cells, INF), prev(cells, INF);
        int pathTime = dijkstra(maze, i, exitCell-1, dist, prev);
        if(pathTime <= timer) mice++;
    }

    cout << mice << "\n";
}
