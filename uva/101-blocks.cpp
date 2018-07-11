//https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=3&page=show_problem&problem=37

#include <bits/stdc++.h>
using namespace std;

/* TIL:
*   1 - ...
*   2 - ...
*   3 - ...
*/

void printWorld(const vector<stack<int>> &bworld){

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

vector<string> parseCmd(const string cmd){
	
	vector<string> parsedCmd;

	stringstream ss(cmd);
	string dummy;
	while(ss >> dummy){
		parsedCmd.push_back(dummy);
	}

	return parsedCmd;
}

void restore(vector<stack<int>> &bworld, int x){

	while(bworld[x].size() > 1){
		int c = bworld[x].top();
		bworld[x].pop();

		bworld[c].push(c);
	}

}

void moveOnto(vector<stack<int>> &bworld, int a, int b){

	//restore pile of a and b
	restore(bworld, a);
	restore(bworld, b);

	//place a on top of b
	bworld[b].push(a);
	bworld[a].pop();

}

void moveOver(vector<stack<int>> &bworld, int a, int b){

}

void pileOnto(vector<stack<int>> &bworld, int a, int b){

}

void pileOver(vector<stack<int>> &bworld, int a, int b){

}


void processCommand(vector<stack<int>> &bworld, string cmd){

	cout << "\nPROCESSNG CMD: " << cmd << "\n";

	vector<string> parsedCmd = parseCmd(cmd);

	//validations
	if(parsedCmd.size() != 4)
		return;

	if(parsedCmd[1] == parsedCmd[3])
		return;


	if(parsedCmd[0].compare("move") == 0){
		if(parsedCmd[0].compare("onto") == 0)
			moveOnto(bworld, stoi(parsedCmd[1]), stoi(parsedCmd[3]));

		if(parsedCmd[0].compare("over") == 0)
			moveOver(bworld, stoi(parsedCmd[1]), stoi(parsedCmd[3]));
	}


	if(parsedCmd[0].compare("pile") == 0){
		if(parsedCmd[0].compare("onto") == 0)
			pileOnto(bworld, stoi(parsedCmd[1]), stoi(parsedCmd[3]));

		if(parsedCmd[0].compare("over") == 0)
			pileOver(bworld, stoi(parsedCmd[1]), stoi(parsedCmd[3]));
	}

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
    
    cin.ignore();
    
    string cmd;
    while(true){
    	
    	getline(cin, cmd);
    	if(cmd == "quit") break;

    	processCommand(bworld, cmd);
    }

    printWorld(bworld);
}
