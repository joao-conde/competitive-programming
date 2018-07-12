//https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=3&page=show_problem&problem=37

#include <bits/stdc++.h>
using namespace std;

/* TIL:
*   1 - ...
*   2 - ...
*   3 - ...
*/

void printWorld(const vector<stack<int>> &bworld){

	cout << "\n---BLOCK WORLD---\n";


	for(int i = 0; i < bworld.size(); i++){
		cout << i << ":";

		string stackStr = "";
		stack<int> auxStack = bworld.at(i);

		while(!auxStack.empty()){
			stackStr = to_string(auxStack.top()) + " " + stackStr;
			auxStack.pop();
		}

		cout << stackStr << "\n";
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


void moveTopTo(vector<stack<int>> &bworld, int a, int b){

	//place a on top of b
	bworld[b].push(a);
	bworld[a].pop();	
}


void movePileTo(vector<stack<int>> &bworld, int a, int b){

	stack<int> auxStack = bworld[a];
	vector<int> pileToMove;

	while(!auxStack.empty()){
		pileToMove.push_back(auxStack.top());
		auxStack.pop();
	}

	for(int i = pileToMove.size() - 1; i >= 0; i++){
		bworld[b].push(pileToMove[i]);
	}

}

void moveOnto(vector<stack<int>> &bworld, int a, int b){
	cout << "MOVE ONTO " << a << " - " << b << "\n";
	//restore pile of a and b
	restore(bworld, a);
	restore(bworld, b);

	moveTopTo(bworld, a, b);

}

void moveOver(vector<stack<int>> &bworld, int a, int b){

	restore(bworld, a);

	moveTopTo(bworld, a, b);

}

void pileOnto(vector<stack<int>> &bworld, int a, int b){

	restore(bworld, b);
	movePileTo(bworld, a, b);

}

void pileOver(vector<stack<int>> &bworld, int a, int b){
	movePileTo(bworld, a, b);
}


void processCommand(vector<stack<int>> &bworld, string cmd){

	vector<string> parsedCmd = parseCmd(cmd);

	//validations
	if(parsedCmd.size() != 4)
		return;

	if(parsedCmd[1].compare(parsedCmd[3]) == 0)
		return;


	if(parsedCmd[0].compare("move") == 0){
		if(parsedCmd[2].compare("onto") == 0)
			moveOnto(bworld, stoi(parsedCmd[1]), stoi(parsedCmd[3]));

		if(parsedCmd[2].compare("over") == 0)
			moveOver(bworld, stoi(parsedCmd[1]), stoi(parsedCmd[3]));
	}


	if(parsedCmd[0].compare("pile") == 0){
		if(parsedCmd[2].compare("onto") == 0)
			pileOnto(bworld, stoi(parsedCmd[1]), stoi(parsedCmd[3]));

		if(parsedCmd[2].compare("over") == 0)
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
