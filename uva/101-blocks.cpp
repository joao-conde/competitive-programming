//https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=3&page=show_problem&problem=37

#include <bits/stdc++.h>
using namespace std;

/* TIL:
*   1 - ...
*   2 - ...
*   3 - ...
*/

void printWorld(vector<stack<int>> bworld){

	cout << "\n---BLOCK WORLD---";
	for(int i = 0; i < bworld.size(); i++){
		cout << "\n" << i << ":";

		stack<int> auxStack = bworld.at(i);
		while(!auxStack.empty()){
			cout << " " << auxStack.top();
			auxStack.pop();
		}
	}
	cout << "\n";

}

int main() {
    
    ios::sync_with_stdio(0); 
    cin.tie();

    int nBlocks;
    cin >> nBlocks;

    vector<stack<int>> bworld;

    for(int i = 0; i < nBlocks; i++){
    	stack<int> stacki;
    	stacki.push(i);
    	bworld.push_back(stacki);
    } 

    printWorld(bworld);


}
