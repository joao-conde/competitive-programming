//https://www.spoj.com/problems/SUMFOUR/

#include <bits/stdc++.h>
using namespace std;

/* TIL:
*   1 - Combinations of 4 single elements are better done combining 2 pairs of elements
*/

int main() {
    
    ios::sync_with_stdio(0); 
    cin.tie();

    int listSize, quadruplets = 0;
    vector<long long> listA, listB, listC, listD;
    vector<long long> sumsPairsAB, sumsPairsCD; 

    //Read lists' values
    cin >> listSize;
    for(int i = 0; i < listSize; i++){
        long long a, b, c, d;
        cin >> a >> b >> c >> d;
        
        listA.push_back(a);
        listB.push_back(b);
        listC.push_back(c);
        listD.push_back(d);
    }

    //Make pairs of AB and CD
    for(int j = 0; j < listSize; j++){
        for(int l = 0; l < listSize; l++){
            sumsPairsAB.push_back(listA[j] + listB[l]);
            sumsPairsCD.push_back(listC[j] + listD[l]);
        }
    }

    //Make pairs of AB and CD pairs counting those whoose sum equals 0
    for(int j = 0; j < sumsPairsAB.size(); j++){
        for(int k = 0; k < sumsPairsCD.size(); k++){
            if(sumsPairsAB[j] + sumsPairsCD[k] == 0)
                quadruplets++;
        }
    }

    cout << quadruplets << "\n";

}
