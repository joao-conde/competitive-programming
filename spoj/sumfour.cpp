//https://www.spoj.com/problems/SUMFOUR/

#include <bits/stdc++.h>
using namespace std;

/* TIL:
*   1 - Combinations of 4 single elements are better done combining 2 pairs of elements
*/


int main() {
    
    ios::sync_with_stdio(0); 
    cin.tie();

    int listSize; cin >> listSize;
    vector<pair<int, int>> pairsAB, pairsCD; 

    for(int i = 0; i < listSize; i++){
        int a, b, c, d;
        cin >> a >> b >> c >> d;
        pairsAB.push_back(make_pair(a, b));
        pairsCD.push_back(make_pair(c, d));
    }

    int quadruplets = 0;
    for(int j = 0; j < listSize; j++){
        int sumAB = pairsAB[j].first + pairsAB[j].second;
        for(int k = 0; k < listSize; k++){
            int sumCD = pairsCD[k].first + pairsCD[k].second;
            if(sumAB + sumCD == 0)
                quadruplets++;
        }
    }

    cout << quadruplets << "\n";

}
