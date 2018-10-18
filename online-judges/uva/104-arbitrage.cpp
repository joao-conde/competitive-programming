//https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=3&page=show_problem&problem=40

#include <bits/stdc++.h>

#define INF 1000000000
#define MAX 500

using namespace std;


//use Floyd–Warshall
//adding a third dimension to matrix to store profit rate?!?

void floyd(int g[MAX][MAX], int n){

    for(int i = 0; i < n; i++){
        g[i][i] = 0;
    }

    for(int k = 0; k < n; k++){
        for(int j = 0; j < n; j++){
            if(g[j][k] != INF)
                for(int l = 0; l < n; l++)
                    g[j][l] = min(g[j][l], g[j][k] + g[k][l]);
        }
    }

}


int main() {
    
    ios::sync_with_stdio(0); 
    cin.tie();


    int g[MAX][MAX];
FOR(i,n) FOR(j,n) g[i][j] = INF;

g[0][1] = 2;
g[0][3] = 3;
...

floyd(g, n); 

//Printing distance between each node pair
for (int v1 = 0 ; v1 < g.n; v1++) {
  for (int v2 = 0 ; v2 < g.n; v2++)
    if (g[v1][v2] == INF) cout << "- ";
    else cout << g[v1][v2] << " ";
  cout << endl;
}



}
