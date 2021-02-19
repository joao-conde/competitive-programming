//https://csacademy.com/contest/archive/task/adaptive-binary-search/

#include <bits/stdc++.h>
using namespace std;


/* TIL:
*   1 - binary search algorithm for problems like this, well explained at:
*        https://www.quora.com/What-is-the-correct-approach-to-solve-the-SPOJ-problem-Aggressive-cow
*
*    2 - we know the possible smallest value (1) and the biggest one (N)
*
*    3 - we also know that if a value X of distance cannot be satisfied then for any Y > X
*        Y cannot be satisfied aswell -> this property is called monotonicity condition and
*        it is necessary for binary search
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

    while(lb <= ub){

        mid = (lb + ub) / 2;

        if(query(mid) == 0) //X smaller than guess
            ub = mid - 1;
        else //X bigger than guess
            lb = mid + 1;

    }

    cout << "A " << lb << endl;

}
