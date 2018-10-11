//https://www.spoj.com/problems/PPATH/

#include <bits/stdc++.h>
using namespace std;

/* TIL:
*   1 - ...
*   2 - ...
*   3 - ...
*/

#define MAX 10000
#define SQRT_MAX 320
#define INF 1000000
#define TREE_LVLS 50 
#define DIGITS 10

int isPrime[MAX]; //0 - prime ; 1 - not prime
int graph[MAX][TREE_LVLS]; 

void bfs(int source, int dest, vector<int>& dist) {
    queue<int> q;
    dist[source] = 0;
    q.push(source);
    while (!q.empty()) {
        int cur = q.front(); q.pop();
        for (int e : graph[cur]) 
            if (dist[e] == INF) {
                dist[e] = dist[cur] + 1;
                q.push(e);
            }
    }
}


int main() {

    ios::sync_with_stdio(0); 
    cin.tie();

    //sieve
    isPrime[0] = isPrime[1] = 1;
    for(int i = 2; i < SQRT_MAX; i++){
        if(isPrime[i]) continue;

        for(int j = 2*i; j < SQRT_MAX; j+=i){
            isPrime[j] = 1;
        }
    }


    //build graph of possible paths
    for(int i = 0; i < MAX; i++){ //for all possible 4-digit prime numbers
        
        if(isPrime[i]) continue; //not a prime number

        //from left to right, 0 to 3
        int d0, d1, d2, d3;
        d0 = i%10;
        d1 = (i/10) % 10;
        d2 = (i/100) % 10;
        d3 = i/1000;

        //changing all 4 digits to possible digits that make a 4 digit prime
        int childNo = 0;

        //change d0
        for(int j = 0; j < DIGITS; j++){
            int n = d3*1000 + d2*100 + d1*10 + j;
            if(isPrime[n] == 0)
                graph[i][childNo++] = n; //adds child and increments no. 
        }

        //change d1
        for(int j = 0; j < DIGITS; j++){
            int n = d3*1000 + d2*100 + j*10 + d0;
            if(isPrime[n] == 0)
                graph[i][childNo++] = n; //adds child and increments no. 
        }

        //change d2
        for(int j = 0; j < DIGITS; j++){
            int n = d3*1000 + j*100 + d1*10 + d0;
            if(isPrime[n] == 0)
                graph[i][childNo++] = n; //adds child and increments no. 
        }

        //change d3
        for(int j = 0; j < DIGITS; j++){
            int n = j*1000 + d2*100 + d1*10 + d0;
            if(isPrime[n] == 0)
                graph[i][childNo++] = n; //adds child and increments no. 
        }

    }

    
    int testCases; cin >> testCases;
    while(testCases--){
        int srcPrime, dstPrime; 
        cin >> srcPrime >> dstPrime;

        vector<int> dist(MAX, INF);
        bfs(srcPrime, dstPrime, dist);
        cout << dist[dstPrime] << endl;
    }

}
