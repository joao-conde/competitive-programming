//https://www.spoj.com/problems/PARTY/

#include <bits/stdc++.h>
using namespace std;

/* TIL:
*   1 - ...
*   2 - ...
*   3 - ...

https://www.geeksforgeeks.org/knapsack-problem/
This is solvable using the classical Knapsack approach. I am assuming you already know how to do 
that so after you have built the 2D dynamic programming table for this question where rows represent 
the number of parties n and columns represent the budget associated. We know that DP[n][m] represents 
the maximum fun value for the maximum budget m and n parties. Now let us say that the optimal value is K. 
So we want to see now if there is some lesser cost which gives us the same level of fun i.e. K. So just scan 
the last row of the DP table and check the first value DP[n][i] that is equal to K. This i is your optimal cost.

*/

int knapsack01_bottomUp(int val[], int wt[], int c, int n){

	//value for knapsack with c capacity and n weights selected (+1 because '0' case is evaluated)
	int dp[n+1][c+1];
	
	for(int i = 0; i <= n; i++){

		for(int j = 0; j <= c; j++){

			if(i == 0 || j == 0) 
				dp[i][j] = 0;

			else if(wt[i-1] <= j)
				dp[i][j] = max(val[i-1] + dp[i-1][j-wt[i-1]], dp[i-1][j]);

			else 
				dp[i][j] = dp[i-1][j];

		}

	}

	return dp[n][c];
}

int main() {

    ios::sync_with_stdio(0); 
    cin.tie();

    while(true){
		int budget, parties;
		cin >> budget; cin >> parties;

		if(budget == 0 && parties == 0) //end of input
			break;

		//knapsack weights and values
		int fees[parties], funRates[parties], cost, fun;
		for(int i = 0; i < parties; i++){
			cin >> cost; cin >> fun;
			fees[i] = cost;
			funRates[i] = fun;
		}

		cout << knapsack01_bottomUp(funRates, fees, budget, parties) << "\n";
    }

}
