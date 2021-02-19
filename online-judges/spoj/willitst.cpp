//https://www.spoj.com/problems/WILLITST/

#include <bits/stdc++.h>
using namespace std;

/*
 *     If it cycles then it never ends, if not it does.
 */

bool checkCycle(unsigned long long n){
    vector<int> nValues;

    while(n > 1){

        if(find(nValues.begin(), nValues.end(), n) != nValues.end())
            return true;

        nValues.push_back(n);

        if(n % 2 == 0){
            n = n/2;
        }
        else{
            n = 3*n + 3;
        }
    }

    return false;
}


int main() {
    ios::sync_with_stdio(0);
    cin.tie();

    unsigned long long n;
    cin >> n;
    cout << (checkCycle(n) ? "NIE" : "TAK") << "\n";
}
