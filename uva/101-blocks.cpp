#include <bits/stdc++.h>
using namespace std;


/*
 *	Restore blocks stacked on top of block b to original positions.
 */
void restore(int b, vector<stack<int>> &bworld, vector<int> &bpositions){

	while(bworld[bpositions[b]].top() != b){
		int top = bworld[bpositions[b]].top();

		bworld[top].push(top);

		bpositions[top] = top;
		bworld[bpositions[b]].pop();
	}
}

/*
 *	Moves block a to the stack of b. Requires a to be top of its stack.
 */
void moveBlock(int a, int b, vector<stack<int>> &bworld, vector<int> &bpositions){

	bworld[bpositions[a]].pop();

	bworld[bpositions[b]].push(a);
	bpositions[a] = bpositions[b];

}


/*
 *	Moves the pile of blocks consisting of block a and those above it on top of block b.
 *	Pile of blocks retains its order.
 */
void movePile(int a, int b, vector<stack<int>> &bworld, vector<int> &bpositions){

	vector<int> pile;

	if(bpositions[a] == bpositions[b]) return;

	while(bworld[bpositions[a]].top() != a){
		pile.push_back(bworld[bpositions[a]].top());
		bworld[bpositions[a]].pop();
	}

	pile.push_back(a);
	bworld[bpositions[a]].pop();


	for(int i = pile.size()-1; i >= 0; i--){
		bworld[bpositions[b]].push(pile[i]);
		bpositions[pile[i]] = bpositions[b];
	}
	
}


/*
 *	Moves a onto b, restoring any blocks above both a and b first.
 */
void moveOnto(int a, int b, vector<stack<int>> &bworld, vector<int> &bpositions){
	restore(a, bworld, bpositions);
	restore(b, bworld, bpositions);
	moveBlock(a, b, bworld, bpositions);
}

/*
 *	Moves a onto b, restoring any blocks above a first.
 */
void moveOver(int a, int b, vector<stack<int>> &bworld, vector<int> &bpositions){
	restore(a, bworld, bpositions);
	moveBlock(a, b, bworld, bpositions);
}

/*
 *	Moves the pile of blocks a onto b, first restoring blocks above b.
 */
void pileOnto(int a, int b, vector<stack<int>> &bworld, vector<int> &bpositions){
	restore(b, bworld, bpositions);
	movePile(a, b, bworld, bpositions);
}

/*
 *	Moves the pile of blocks a onto b stack.
 */
void pileOver(int a, int b, vector<stack<int>> &bworld, vector<int> &bpositions){
	movePile(a, b, bworld, bpositions);
}


/*
 *	Prints block world in an human friendly way.
 */
void printWorld(const vector<stack<int>> &bworld){

	for(int i = 0; i < bworld.size(); i++){
		cout << i << ":";

		string stackStr = "";
		stack<int> auxStack = bworld.at(i);

		while(!auxStack.empty()){
			stackStr = " " + to_string(auxStack.top()) + stackStr;
			auxStack.pop();
		}

		cout << stackStr << "\n";
	}
}


/*
 *	Parses the input string as an array of arguments.
 */
vector<string> parseCmd(const string cmd){
	
	vector<string> parsedCmd;

	stringstream ss(cmd);
	string dummy;
	while(ss >> dummy){
		parsedCmd.push_back(dummy);
	}

	return parsedCmd;
}


/*
 *	Processes the arguments executing correct movements.
 */
void processCommand(vector<stack<int>> &bworld, vector<int> &bpositions, string cmd){

	vector<string> parsedCmd = parseCmd(cmd);

	//valid command size
	if(parsedCmd.size() != 4) return;

	//valid arguments -> a != b
	if(parsedCmd[1].compare(parsedCmd[3]) == 0)	return;

	//a and b must be valid integers
	int a, b;
	a = stoi(parsedCmd[1]);
	b = stoi(parsedCmd[3]);
	

	int aPos = bpositions[a],
		bPos = bpositions[b];

	//a can't be on b stack
	if(aPos == bPos) return;


	if(parsedCmd[0].compare("move") == 0){
		if(parsedCmd[2].compare("onto") == 0)
			moveOnto(a, b, bworld, bpositions);

		if(parsedCmd[2].compare("over") == 0)
			moveOver(a, b, bworld, bpositions);
	}


	if(parsedCmd[0].compare("pile") == 0){
		if(parsedCmd[2].compare("onto") == 0)
			pileOnto(a, b, bworld, bpositions);

		if(parsedCmd[2].compare("over") == 0)
			pileOver(a, b, bworld, bpositions);
	}

}

int main() {
    
    ios::sync_with_stdio(0); 
    cin.tie();

    int nBlocks;
    cin >> nBlocks;

    vector<stack<int>> bworld;
    vector<int> bpositions;

    //initialize world
    for(int i = 0; i < nBlocks; i++){
    	
    	stack<int> stacki;
    	stacki.push(i);

    	bworld.push_back(stacki);
    	bpositions.push_back(i);

    }

    string cmd;
    while(true){
    	
    	getline(cin, cmd);
    	if(cmd == "quit") break;

    	processCommand(bworld, bpositions, cmd);
    }

    printWorld(bworld);
}
