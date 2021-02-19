//https://www.spoj.com/problems/TRIKA/

#include <bits/stdc++.h>
using namespace std;


int main() {

    ios::sync_with_stdio(0);
    cin.tie();

    int rows, cols, x0, y0;
    cin >> rows >> cols >> x0 >> y0;

    //problem input is 1-indexed (what? xD)
    x0--;
    y0--;

    int dp[rows][cols], powers[rows][cols];
    for(int i = 0; i < rows; i++){
        for(int j = 0; j < cols; j++){
            cin >> powers[i][j];
        }
    }

    //Abotrika's starting cell
    dp[x0][y0] = powers[x0][y0];


    //cells to the right of Abotrika
    for(int i = y0 + 1; i < cols; i++)
        dp[x0][i] = dp[x0][i-1] - powers[x0][i];


    //cells down Abotrika
    for(int j = x0 + 1; j < rows; j++)
        dp[j][y0] = dp[j-1][y0] - powers[j][y0];


    //bottom-up dp matrix fill
    for(int i = x0 + 1; i < rows; i++){
        for(int j = y0 + 1; j < cols; j++){
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) - powers[i][j];
        }
    }

    if(dp[rows-1][cols-1] < 0){
        cout << "N\n";
    }
    else{
        cout << "Y " << dp[rows-1][cols-1] << "\n";
    }

}
