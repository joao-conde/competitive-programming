//https://www.spoj.com/problems/PARTY/

#include <bits/stdc++.h>
using namespace std;

/* TIL:
*   1 - Knapsack 0/1 problem: for a set of items with different weights and values find the optimal subset of items 
*   that maximizes value and minimizes weight
*
*   2 - It's '0/1' because you either choose the item or you don't (there problems where partial items can be envolved)
*
*	3 - Dynamic programming is basically using memoization to avoid repeating computations already made, storing these values
*	in a data structure with linear (O(1)) access time 
*
*	4 - Useful link: https://www.geeksforgeeks.org/knapsack-problem/
*
*/


/*
 *	Bottom up approach: each following computation needs a previous value and instead of re-computing it we
 *	access the dp matrix in linear time
 */
pair<int,int> knapsack01_bottomUp(int val[], int wt[], int c, int n){

	//matrix storing computations already made
	//ranges from 0 to N and from 0 to C thus the +1
	int dp[n+1][c+1];
	
	for(int i = 0; i <= n; i++){

		for(int j = 0; j <= c; j++){

			//base case: with 0 items or a maximum capacity of 0 we get a value of 0
			if(i == 0 || j == 0) 
				dp[i][j] = 0;

			/*
			 *	if the weight of the item is smaller than our capacity we check where do we get the max value
			 *	if we include it we get the value of that item plus the value of the remaining items with capacity 
			 *	minus the weight of the item we inserted
			 *	if not we simply check the value for the remaining items, same capacity
			 */
			else if(wt[i-1] <= j)
				dp[i][j] = max(val[i-1] + dp[i-1][j-wt[i-1]], dp[i-1][j]);

			//weight of item exceeds maximum capacity so we can never pick it
			else 
				dp[i][j] = dp[i-1][j];

		}

	}

	/*
	 * dp[n][c] contains the maximum value solution but also the maximum cost one without exceeding the capacity.
	 * Knowing the best value we search the matrix column where that value is max (column n) with the smallest cost possible
	 * thus getting the highest value solution at the lowest possible cost.
	 */
	pair<int,int> val_wt = make_pair(c, dp[n][c]);
	for (int k = 0; k <= c; k++){
		if (dp[n][k] == dp[n][c]){
			val_wt.first = k;
			break;
		}
	}

	return val_wt;
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

		//knapsack 0/1 bottom up approach
		pair<int,int> fun_cost = knapsack01_bottomUp(funRates, fees, budget, parties);
		cout << fun_cost.first << " " << fun_cost.second << "\n";
    }

}
