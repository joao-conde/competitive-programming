//https://www.spoj.com/problems/FOXLINGS/

#include <bits/stdc++.h>
using namespace std;

struct DisjointSet{

    long vertexes;
    unordered_map<long, long> parent, degree;

    DisjointSet(long n){
        vertexes = n;
    }

    long getParent(long vertex){

        if(parent.find(vertex) != parent.end()){
            if(parent[vertex] != vertex){
                parent[vertex] = getParent(parent[vertex]);
                return parent[vertex];
            }
        }

        else{
            parent.insert({vertex, vertex});
            degree.insert({vertex, 1});
        }

        return vertex;
    }

    void union_set(long vertexA, long vertexB){

        long parentA = getParent(vertexA),
                parentB = getParent(vertexB);

        if(parentA == parentB) return;

        if(degree[parentA] > degree[parentB]){
            parent[parentB] = parentA;
            degree[parentA] += degree[parentB]; 
        }
        else{
            parent[parentA] = parentB;
            degree[parentB] += degree[parentA];
        }
    }

    long getTotalComponent(){

        unordered_set<long> total;

        for(auto it = parent.begin(); it != parent.end(); it++){
            total.insert(getParent(it->first));
        }

        return vertexes - parent.size() + total.size();
    }

};

int main(){
    
    ios::sync_with_stdio(0); 
    cin.tie();

    long foxlings, friendships;
    cin >> foxlings >> friendships;

    DisjointSet dsu(foxlings);

    for(int i = 0; i < friendships; i++){
        long ai, bi; cin >> ai >> bi;
        dsu.union_set(ai, bi);
    }

    cout << dsu.getTotalComponent() << "\n";
    
}