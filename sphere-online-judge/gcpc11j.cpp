//http://www.spoj.com/problems/GCPC11J/

#include <iostream>



using namespace std;

int main(){

    int test_cases, ttl, computers, node1, node2;
    cin >> test_cases;

    for(int i = 0; i < test_cases; i++){
        cin >> computers;
        //use belman ford, get maximum value, that = TTL, that node is router, if next iter has smaller ttl, thats the router
        //do untill no more nodes, print TTL
        ttl = -1;
        for(int j = 0; j < computers - 1; j++){
            cin >> node1;
            cin >> node2;
        }

        cout << "TEST CASE " << i+1 << ": " << ttl << endl;

    }


    
    return 0;
}