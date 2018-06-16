//http://www.spoj.com/problems/CANDY3/

#include <bits/stdc++.h> //Includes ALL c++ files needed

using namespace std;

/* TLDR:
*   1 - module operation properties TODO: UNDERSTAND THIS
*/

int main(){

    ios::sync_with_stdio(0); //Input and output become more efficient.
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