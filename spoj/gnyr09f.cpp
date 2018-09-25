//https://www.spoj.com/problems/GNYR09F/

#include <bits/stdc++.h>
using namespace std;

int main() {

    ios::sync_with_stdio(0); 
    cin.tie();

    int dp[100][100][2];

    for(int i = 0; i < 100; i++){
        for(int j = 0; j < 2; j++){
            dp[0][i][j] = 0; //every 0 length string as 0 adj()
        }
    }
    
    dp[1][0][0] = dp[1][0][1] = 1; //base case

    for(int i = 1; i < 100; i++){
        for(int j = 0; j < 100; j++){
            dp[i][j][0] = dp[i-1][j][0] + dp[i-1][j][1];

            if(j > 0) dp[i][j][1] = dp[i-1][j-1][1];

            dp[i][j][1] += dp[i-1][j][0];
        }
    }

    int dataSets; cin >> dataSets;
    while(dataSets--){

        int dataSetID, stringLen, adjBitCnt;
        cin >> dataSetID >> stringLen >> adjBitCnt;

        cout << "\n" << dataSetID << " : " << stringLen << " : " << adjBitCnt << " : " << dp[stringLen][adjBitCnt][0] <<  " ---- " << dp[stringLen][adjBitCnt][1] << endl;
    }

}
