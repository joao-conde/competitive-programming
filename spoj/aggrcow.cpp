//https://www.spoj.com/problems/AGGRCOW/

#include <bits/stdc++.h>
using namespace std;


/* TIL:
*   1 - binary search algorithm for problems like this, well explained at:
*		https://www.quora.com/What-is-the-correct-approach-to-solve-the-SPOJ-problem-Aggressive-cow
*
*	2 - we know the possible smallest value (0, all cows in sequential stalls) and the biggest one
*		(max distance stall minus the first, simulatng 2 cows at each edge)
*
*	3 - we also know that if a value X of distance cannot be satisfied then for any Y > X
*		Y cannot be satisfied aswell -> this property is called monotonicity condition and 
*		it is necessary for binary search
*
*	4 - all we need is a function that checks if a given X can be satisfied given the number of cows
*		and stalls and each of their distances
*/


/*
 *	Checks wether or not C cows fit the stalls separated by at least dis from each other.
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

    	//sort stalls to properly calculate distances
    	sort(stalls.begin(), stalls.end());

    	//binary search: min = 0, max = distance from first to last stall
        int lb = 0, hb = stalls[nStalls - 1] - stalls[0], mid;
 
        //find the last occurence of a possible minimum value - maximized minimum distance
        while(hb - lb > 1){
			
			//sum of lb avoids overflow
            mid = lb + (hb - lb) / 2;
 
            if(canSeparateCowsBy(mid, stalls, cows)){
                lb = mid;
            } else {
                hb = mid;
            }
        }
 
        cout << lb << "\n";

    }

}
