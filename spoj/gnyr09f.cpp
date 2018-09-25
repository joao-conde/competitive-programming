//https://www.spoj.com/problems/GNYR09F/

#include <bits/stdc++.h>
using namespace std;

int main() {

    ios::sync_with_stdio(0); 
    cin.tie();

    int dp[100+2][100+2][2];

    dp[1][0][0] = dp[1][0][1] = 1; //base case: 1 way only of getting a 1 length string and 0 adj()

    for(int i = 2; i <= 100; i++){
        for(int j = 0; j <= 100; j++){
            dp[i][j][0] = dp[i-1][j][0] + dp[i-1][j][1];

            if(j > 0) dp[i][j][1] = dp[i-1][j-1][1];

            dp[i][j][1] += dp[i-1][j][0];
        }
    }

    int dataSets; cin >> dataSets;
    while(dataSets--){

        int dataSetID, stringLen, adjBitCnt;
        cin >> dataSetID >> stringLen >> adjBitCnt;

        cout << dataSetID << " " << dp[stringLen][adjBitCnt][0] + dp[stringLen][adjBitCnt][1] << endl;
    }

}
