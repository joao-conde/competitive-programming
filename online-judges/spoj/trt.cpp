 //https://www.spoj.com/problems/TRT/

#include <bits/stdc++.h>
using namespace std;

/* TIL:
*   1 - Top down approach DP useful when there is a clear recursive solution
*/


int treats[2001], memo[2001][2001];

/*
    Recursive solution to the problem
    Tries to sell left whine and right whine, picks the maximum possible value
*/
int computeProfit(int leftTrtIdx, int rightTrtIdx, int year){

    if(memo[leftTrtIdx][rightTrtIdx] != -1) return memo[leftTrtIdx][rightTrtIdx];

    if(leftTrtIdx > rightTrtIdx) return 0;

    return memo[leftTrtIdx][rightTrtIdx] = max(
        computeProfit(leftTrtIdx+1, rightTrtIdx, year + 1) + year * treats[leftTrtIdx],
        computeProfit(leftTrtIdx, rightTrtIdx-1, year + 1) + year * treats[rightTrtIdx]
    );

}

int main() {

    ios::sync_with_stdio(0);
    cin.tie();

    memset(memo, -1, sizeof(memo));

    int nTreats; cin >> nTreats;

    for(int i = 0; i < nTreats; i++){
        cin >> treats[i];
    }

    cout << computeProfit(0, nTreats-1, 1) << endl;
}
