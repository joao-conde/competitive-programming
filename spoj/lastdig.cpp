//https://www.spoj.com/problems/LASTDIG/

#include <bits/stdc++.h>
using namespace std;

/* TIL:
*   1 - Again: find patterns and alternative solutions to avoid high complexity
*   2 - Modulo arithmetic is super powerful and useful
*/

vector<int> computeEndingPattern(int base){
    vector<int> pattern;

    int i = 1;
    while(true){
	   	int lastDigit = ((int)pow(base,i)) % 10;

	   	if(find(pattern.begin(), pattern.end(), lastDigit) != pattern.end())
	   		break;

    	pattern.push_back(lastDigit);
    	i++;
    }

    //last element should be first to facilitate calculating pattern index using modulo
    pattern.insert(pattern.begin(), pattern.at(pattern.size()-1));
    pattern.pop_back();

    return pattern;
}

int main() {
    ios::sync_with_stdio(0); 
    cin.tie();

    int testCases, base, exp;
    cin >> testCases;

    for(int i = 0; i < testCases; i++){
    	cin >> base; cin >> exp;

    	if(exp == 0){
    		cout << "1\n";
    		continue;
    	}
    	
    	vector<int> endPattern = computeEndingPattern(base);
    	cout << endPattern.at(exp % endPattern.size()) << "\n";
    }	

}
