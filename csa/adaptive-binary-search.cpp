//https://csacademy.com/contest/archive/task/adaptive-binary-search/

#include <bits/stdc++.h>
using namespace std;


/* TIL:
*   1 - binary search algorithm for problems like this, well explained at:
*		https://www.quora.com/What-is-the-correct-approach-to-solve-the-SPOJ-problem-Aggressive-cow
*
*	2 - we know the possible smallest value (1) and the biggest one (N)
*
*	3 - we also know that if a value X of distance cannot be satisfied then for any Y > X
*		Y cannot be satisfied aswell -> this property is called monotonicity condition and 
*		it is necessary for binary search
*/


int query(int solution){
	
	int result = 0;
	
	cout << "Q " << solution << endl;
	cin >> result;

	return result;
}

int main() {
    ios::sync_with_stdio(0); 
    cin.tie();

    int n;
    cin >> n;

    int lb = 1, ub = n, mid;

    while(ub - lb > 1){

    	mid = (lb + ub) / 2;

    	//cout << "lb " << lb << " mid " << mid << " ub " << ub << endl;

    	//X smaller than guess
    	if(query(mid) == 0)
    		ub = mid;
    	//X bigger than guess
    	else lb = mid;

    }

    cout << "A " << ub << "\n";

}
