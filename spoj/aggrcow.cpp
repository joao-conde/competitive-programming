//https://www.spoj.com/problems/AGGRCOW/

#include <bits/stdc++.h>
using namespace std;


/*
https://en.wikipedia.org/wiki/Pigeonhole_principle

https://www.quora.com/What-is-the-correct-approach-to-solve-the-SPOJ-problem-Aggressive-cow


use binary search to find largest min distance
basically we know the answer ranges from 0 (all cows together) to N-1 (2 cows one at each edge)
so using binary search we find that value X 
thus we need a function to determine if with C cows you can place them spaced by X (or more)
*/

/*
 *	Checks wether or not C cows fit separated by at least dis from each other.
 */
bool canSeparateCowsBy(int dis, vector<int> stalls, int cows){

	//cow placed at first stall (always at least 2 cows)
	int curIdx = 0;
	cows--;

	for(int i = 0; i < stalls.size(); i++){

		//this cow is placed at least 'dis' from the last one
		if(stalls.at(i) - stalls.at(curIdx) >= dis){
			//no more cows to place -> it is possible
			if(--cows == 0) return true;
			curIdx = i;
		}

	}

	//not all cows were placed -> not possible with minimum distance of 'dis'
	return false;
}


int main() {

    ios::sync_with_stdio(0); 
    cin.tie();

    int testCases, nStalls, cows, dummy;
    cin >> testCases;

    while(testCases--){

    	cin >> nStalls; cin >> cows;

    	vector<int> stalls;

    	for(int i = 0; i <  nStalls; i++){
    		cin >> dummy;
    		stalls.push_back(dummy);
    	}

    	sort(stalls.begin(), stalls.end());

    	cout << "CAN SEPARATE COWS: " << canSeparateCowsBy(4, stalls, cows) << "\n";
    	//TODO: binary search between 0 and N
    }

}
