//https://www.spoj.com/problems/CSTREET/

#include <bits/stdc++.h>
using namespace std;

/* TIL:
*   1 - ...
*   2 - ...
*   3 - ...
*/


#define MK              make_pair 
#define COST            first
#define V1              second.first
#define V2              second.second

typedef pair<int,int> PII;

const int& INF = numeric_limits<int>::max();

class elGraph: public deque< pair<int, PII> >{  // Edge List
public:
	int n;
	elGraph(const int& s):deque< pair<int, PII> >(){n = s;}
	void addEdge(const int& src, const int& dst, const int& c){
		this->push_back(MK(c, PII(src, dst)));
	}
};

struct node{ int p, rank, number; };
class uf: public vector<node>{
public:
	int sets;

	uf(int s):vector<node>(s){
		sets = s;
		uf& me = *this;
		for(int i = 0; i < s; i++)
			me[i] = {i,0,1};
	}

	void link(const int& x, const int& y) {
		uf& me = *this;
		if(x == y) return;
		if (me[x].rank <= me[y].rank) {
			me[x].p = y;
			--sets;
			me[y].number += me[x].number;
			if (me[x].rank == me[y].rank)
				me[y].rank++;
		} else link(y, x);
	}

	int find_set(const int& x) {
		uf& me = *this;
		if (x != me[x].p)
			me[x].p = find_set(me[x].p);
		return me[x].p;
	}
	//Esta funcao pode nao ser importante
	int find_length(const int& x) {
		uf& me = *this;
		return me[find_set(me[x].p)].number;
	}

	void union_set(const int& x, const int& y) {
		link(find_set(x), find_set(y));
	}
};

int kruskal(elGraph g, vector<bool>& mst){
	sort(g.begin(), g.end());
	mst = vector<bool>(g.size(), false);

	uf s(g.n);
	int minimum = 0;
	for(int i = 0; i < g.size(); i++){
		if(s.find_set(g[i].V1) != s.find_set(g[i].V2)) {
			s.union_set(g[i].V1, g[i].V2);
			mst[i] = true;
			minimum += g[i].COST;
		}
	}
	return minimum;
}

int main() {
    
    ios::sync_with_stdio(0); 
    cin.tie();


    int testCases; cin >> testCases;
    while(testCases--){
        int price, mainBuildings, streets;
        cin >> price >> mainBuildings >> streets;

        vector<bool> mst;
        elGraph g(mainBuildings);
        for(int i = 0; i < streets; i++){
            int a, b, c;
            cin >> a >> b >> c;
            g.addEdge(a, b, c);
            g.addEdge(b, a, c);
        }

        cout << price * kruskal(g, mst) << endl;
        
    }
    
}
