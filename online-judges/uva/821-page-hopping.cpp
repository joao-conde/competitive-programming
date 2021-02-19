//https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=762

#include <bits/stdc++.h>
using namespace std;

#define INF 1000000000

/*
 * Breadth-First-Search -> O(E + V)
 *
 * Calculates the shortest path between a source node and all other nodes in a graph
 * defined as an adjacency list with all edges having the same cost (1).
 *
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

/*
 * Computes the average shortest path of a node to all other ones
 */
double computeAverageShortestPath(const vector<vector<int>> &g, int src){

    double avg = 0, undefined = 0;
    vector<int> dist(g.size(), INF);

    bfs(g, src, dist);

    for(int i = 0; i < dist.size(); i++){

        if(i == src) continue;

        if(dist.at(i) == INF){
            undefined++;
            continue;
        }

        avg += dist[i];

    }

    avg /= (g.size() - undefined - 1);

    return avg;
}


/*
 *  Builds a graph based on a edges vector assuming each 2 elements are in the format of src->dest
 */
vector<vector<int>> buildGraph(const vector<int> &edges){

    int gSize = *max_element(edges.begin(), edges.end());

    vector<vector<int>> graph(gSize);

    for(int i = 0; i < edges.size(); i+=2){
        graph[edges[i]-1].push_back(edges[i+1]-1);
    }

    return graph;
}


int main() {
    ios::sync_with_stdio(0);
    cin.tie();

    int src, dest, n = 1;
    while(true){

        cin >> src; cin >> dest;

        if(src == 0 && dest == 0) break;

        vector<int> edges;
        edges.push_back(src);
        edges.push_back(dest);

        while(true){
            cin >> src; cin >> dest;

            if(src == 0 && dest == 0) break;

            edges.push_back(src);
            edges.push_back(dest);
        }

        vector<vector<int>> graph = buildGraph(edges);


        double avg = 0, undefined = 0;
        for(int i = 0; i < graph.size(); i++){
            if(graph[i].size() != 0)
                avg += computeAverageShortestPath(graph, i);
            else
                undefined++;
        }

        avg /= (graph.size() - undefined);

        cout << setprecision(3) << fixed << "Case " << n << ": average length between pages = " << avg << " clicks\n";
        n++;
    }

}
