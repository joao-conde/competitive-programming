//http://www.spoj.com/problems/CANDY3/

#include <bits/stdc++.h>

using namespace std;

/* TIL:
*   1 - modulo operation: rather than summing all then applying modulo it is possible to
*   apply modulo to each of the components you're adding and sum the modulos instead.
*   In the end add the modulos and do modulo of the sum of modulos.
*
*   So if you want to know if (x1 + x2 + x3 + x4) modulo 4 is 0, rather than add all x's and then
*   do modulo 0 (if x's are large the sum is gigantic and may not fit in memory), do modulo for each x
*   and sum the modulos, in the end apply modulo to the sum and check if it is 0.
*   
*   As a result you get a much smaller sum since the added numbers go from 0 to modulo-1
*   In this problem adding all and doing modulo in the end would not work.
*/

int main(){

    ios::sync_with_stdio(0);
    cin.tie();

    int test_cases;
    cin >> test_cases;

    for(int i = 0; i < test_cases; i++){

        long long dummy, children, candies = 0;
        cin >> children;

        for(int k = 0; k < children; k++){
            cin >> dummy;
            candies = (candies + dummy) % children;
        }

        cout << ((candies % children != 0) ? "NO" : "YES") << endl;

    }

    return 0;
}
