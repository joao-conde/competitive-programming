//https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=3&page=show_problem&problem=36

#include <bits/stdc++.h>
using namespace std;


int computeCycleLength(int n){

	if(n < 1) return 0;

	//Ending 1 counts
	int cycles = 1;

	while(n > 1){

		if(n % 2 != 0)
			n = 3*n + 1;
		else
			n = n/2;

		cycles++;
	}

	return cycles;
}

int main() {

    ios::sync_with_stdio(0); 
    cin.tie();

    int i, j;

    while(cin >> i && cin >> j){
    	
    	// i > j may be possible
    	int lb = min(i,j), ub = max(i,j);

    	int maxCycleLength = -1, dummy;

    	while(lb <= ub){

    		dummy = computeCycleLength(lb);

    		if(maxCycleLength < dummy) maxCycleLength = dummy;

    		lb++;
    	}

       	cout << i << " " << j << " " << maxCycleLength << "\n";
    }
   
}
