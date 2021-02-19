//https://www.spoj.com/problems/MISERMAN/

#include <bits/stdc++.h>
using namespace std;


int dp[105][105];

int main() {

    ios::sync_with_stdio(0);
    cin.tie();

    int cities, busesPerCity;
    cin >> cities >> busesPerCity;


    //build fares per bus per city grid
    vector< vector<int> > fares;
    for(int i = 0; i < cities; i++){
        vector<int> faresPerCityBus;
        for(int j = 0; j < busesPerCity; j++){
            int busFare; cin >> busFare;
            faresPerCityBus.push_back(busFare);
        }
        fares.push_back(faresPerCityBus);
    }


    for(int j = 0; j < busesPerCity; j++){
        dp[0][j] = fares[0][j];
    }

    //dp filling, bottom-up
    for(int i = 1; i < cities; i++){
        for(int j = 0; j < busesPerCity; j++){

            if(j == 0){
                dp[i][j] = min(dp[i-1][j], dp[i-1][j+1]) + fares[i][j];
            }
            else if(j == busesPerCity - 1){
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + fares[i][j];
            }
            else{
                dp[i][j] = min(dp[i-1][j-1], min(dp[i-1][j], dp[i-1][j+1])) + fares[i][j];
            }

        }
    }


    int min = 1000000000;
    for(int j = 0; j < busesPerCity; j++){
        if(dp[cities-1][j] < min) min = dp[cities-1][j];
    }

    cout << min << endl;
}
