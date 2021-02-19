//https://www.spoj.com/problems/EIGHTS/

#include <bits/stdc++.h>
using namespace std;


/*
 *    Sequence of '888' terminated numbers follows an Arithmetc Progression
 */
unsigned long long computeAP(unsigned long long k){
    return 192 + (k-1)*250;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie();

    int testCases;
    unsigned long long k;
    cin >> testCases;

    for(int i = 0; i < testCases; i++){
        cin >> k;
        cout << computeAP(k) << "\n";
    }

}
