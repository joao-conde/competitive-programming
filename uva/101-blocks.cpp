//https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=3&page=show_problem&problem=37

#include <bits/stdc++.h>
using namespace std;

void printWorld(const vector<stack<int>> &bworld, const vector<int> &bPositions){

	for(int i = 0; i < bworld.size(); i++){
		cout << i << ": ";

		string stackStr = "";
		stack<int> auxStack = bworld.at(i);

		while(!auxStack.empty()){
			stackStr = to_string(auxStack.top()) + " " + stackStr;
			auxStack.pop();
		}

		cout << stackStr << "\n";
	}
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

void restore(vector<stack<int>> &bworld, vector<int> &bPositions, int x){

	int xPos = bPositions[x];

	while(true){
		
		int top = bworld[xPos].top();

		if(top == x) break;

		bworld[xPos].pop();

		bworld[top].push(top);
		bPositions[top] = top;
	}

}


void moveTopTo(vector<stack<int>> &bworld, vector<int> &bPositions, int a, int b){

	int aPos = bPositions[a],
		bPos = bPositions[b];

	//place a on top of b
	bworld[bPos].push(a);
	bworld[aPos].pop();

	bPositions[a] = bPos;	
}


void movePileTo(vector<stack<int>> &bworld, vector<int> &bPositions, int a, int b){

	int aPos = bPositions[a],
		bPos = bPositions[b];

	vector<int> pileToMove;

	while(true){

		int top = bworld[aPos].top();
		bworld[aPos].pop();

		pileToMove.push_back(top);
		
		if(top == a) break;
	}

	for(int i = pileToMove.size() - 1; i >= 0; i--){
		bworld[bPos].push(pileToMove[i]);
	}

}

void moveOnto(vector<stack<int>> &bworld, vector<int> &bPositions, int a, int b){
	restore(bworld, bPositions, a);
	restore(bworld, bPositions, b);
	moveTopTo(bworld, bPositions, a, b);
}

void moveOver(vector<stack<int>> &bworld, vector<int> &bPositions, int a, int b){
	restore(bworld, bPositions, a);
	moveTopTo(bworld, bPositions, a, b);
}

void pileOnto(vector<stack<int>> &bworld, vector<int> &bPositions, int a, int b){
	restore(bworld, bPositions, b);
	movePileTo(bworld, bPositions, a, b);

}

void pileOver(vector<stack<int>> &bworld, vector<int> &bPositions, int a, int b){
	movePileTo(bworld, bPositions, a, b);
}


void processCommand(vector<stack<int>> &bworld, vector<int> &bPositions, string cmd){

	vector<string> parsedCmd = parseCmd(cmd);

	//valid command size
	if(parsedCmd.size() != 4) return;

	//valid arguments -> a != b
	if(parsedCmd[1].compare(parsedCmd[3]) == 0)	return;

	//a and b must be valid integers
	int a, b;
	try{
		a = stoi(parsedCmd[1]);
		b = stoi(parsedCmd[3]);
	}
	catch (const invalid_argument& ia){
		cout << "DISCARD" << endl;
		return;
	}

	int aPos = bPositions[a],
		bPos = bPositions[b];

	//a can't be on b stack
	if(aPos == bPos) return;


	if(parsedCmd[0].compare("move") == 0){
		if(parsedCmd[2].compare("onto") == 0)
			moveOnto(bworld, bPositions, a, b);

		if(parsedCmd[2].compare("over") == 0)
			moveOver(bworld, bPositions, a, b);
	}


	if(parsedCmd[0].compare("pile") == 0){
		if(parsedCmd[2].compare("onto") == 0)
			pileOnto(bworld, bPositions, a, b);

		if(parsedCmd[2].compare("over") == 0)
			pileOver(bworld, bPositions, a, b);
	}

}


int main() {
    
    ios::sync_with_stdio(0); 
    cin.tie();

    int nBlocks;
    cin >> nBlocks;

    vector<int> blockPositions;  /* current position of each block (to ensure O(1) lookup) */
    vector<stack<int>> bworld;	 /*	the block world itself, with stacked blocks */
    for(int i = 0; i < nBlocks; i++){
    	stack<int> stacki;
    	stacki.push(i);
    	bworld.push_back(stacki);

    	blockPositions.push_back(i);
    } 
    
    cin.ignore();
    
    string cmd;
    while(true){
    	
    	getline(cin, cmd);
    	if(cmd == "quit") break;

    	processCommand(bworld, blockPositions, cmd);
    }

    printWorld(bworld, blockPositions);
}
