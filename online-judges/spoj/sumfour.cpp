//https://www.spoj.com/problems/SUMFOUR/

#include <bits/stdc++.h>
using namespace std;


/* TIL:
*   1 - Combinations of 4 single elements are better done combining 2 pairs of elements
*/

void updateFrequency(unordered_map<long long, long> &umap, long long key){

    unordered_map<long long, long>::iterator it = umap.find(key);

    if(it == umap.end()){
        umap.insert(make_pair(key, 1));
    }
    else{
        umap[key]++;
    }

}

int main() {
    
    ios::sync_with_stdio(0); 
    cin.tie();

    int listSize, quadruplets = 0;
    vector<long long> listA, listB, listC, listD;

    vector<long long> keysAB, keysCD;
    unordered_map<long long, long> pairsAB, pairsCD; 

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

    //Make pairs of AB and CD saving their frequency (how many of each pair)
    for(int j = 0; j < listSize; j++){
        for(int l = 0; l < listSize; l++){
            
            long long sumAB = listA[j] + listB[l], sumCD = listC[j] + listD[l];

            keysAB.push_back(sumAB);
            keysCD.push_back(sumCD);

            updateFrequency(pairsAB, sumAB);
            updateFrequency(pairsCD, sumCD);           
        }
    }

    //For binary search
    sort(keysCD.begin(), keysCD.end());

    //Make pairs of AB and CD pairs counting those whose sum equals 0
    for(int j = 0; j < keysAB.size(); j++){

        //Find if and how many values of sumsPairsCD satisfy keysAB[j] + keysCD[mid] = 0 using binary search
        int lb = 0, ub = keysCD.size(), mid = lb + (ub - lb) / 2;

        while(lb <= ub){
            
            mid = lb + (ub - lb) / 2;
            
            if(keysAB[j] + keysCD[mid] == 0){
                quadruplets += pairsCD[keysCD[mid]];
                break;
            }
            else if(keysAB[j] + keysCD[mid] < 0)
                lb = mid + 1;
            else
                ub = mid - 1;
        }

    }

    cout << quadruplets << "\n";
}
