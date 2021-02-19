//https://www.spoj.com/problems/CUBEFR/

#include <bits/stdc++.h>
using namespace std;

#define MAX 1000000

int pos[MAX+1], notCubeFree[MAX+1];
vector<int> cubeFreeNums;

int main() {

    ios::sync_with_stdio(0);
    cin.tie();

    //pre-compute cubefree numbers
    int cubicRootMax = 100;  //roughly cubic root of max
    cubeFreeNums.push_back(1);
    for(int i = 2; i <= cubicRootMax; i++){

        if(notCubeFree[i]) continue;

        cubeFreeNums.push_back(i);

        int cube = i * i * i;
        for(int j = cube; j <= MAX; j += cube){
            notCubeFree[j] = 1;
        }

    }

    int elements = 0;
    for(int i = 1; i <= MAX; i++){
        if(notCubeFree[i] == 0) pos[i] = ++elements;
    }

    int testCases; cin >> testCases;
    for(int t = 1; t <= testCases; t++){
        int n; cin >> n;

        cout << "Case " << t << ": ";

        if(pos[n] != 0)
            cout << pos[n];
        else
            cout << "Not Cube Free";

        cout << "\n";
    }

}
