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

    //For binary search: searching if there is a pair or multiple pair values that satisfie AB + CD = 0
    sort(sumsPairsAB.begin(), sumsPairsAB.end());
    sort(sumsPairsCD.begin(), sumsPairsCD.end());

    //Make pairs of AB and CD pairs counting those whoose sum equals 0
    for(int j = 0; j < sumsPairsAB.size(); j++){

        //Find if and how many values of sumsPairsCD satisfy sumsPairsAB + sumsPairsCD[j] = 0 using binary search
        int lb = 0, ub = sumsPairsCD.size(), mid = lb + (ub - lb) / 2;
            
        while(lb <= ub){

            mid = mid = lb + (ub - lb) / 2;

            if(sumsPairsCD[mid] + sumsPairsAB[j] == 0){
                //search for neighboor equal values
                quadruplets += count(sumsPairsCD.begin(), sumsPairsCD.end(), sumsPairsAB[j]);
                break;
            }
            else if(sumsPairsCD[mid] + sumsPairsAB[j] < 0)
                lb = mid + 1;
            else
                ub = mid - 1;
        }

    }

    cout << quadruplets << "\n";

}
