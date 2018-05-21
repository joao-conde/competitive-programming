//http://www.spoj.com/problems/NSTEPS/

#include <iostream>

using namespace std;

/*
 *  Receives the coordinates of the point
 *  Returns the number located at (x,y) or -1 if none found
 */
int nsteps(int x, int y){

    int ox = 0, oy = 0, n = 0;
    while(ox <= x + 3){
        
        if(ox == x && oy == y)
            return n;

        //1st step
        ox++; oy++; n++;
        if(ox == x && oy == y)
            return n;

        //2nd step
        ox++; oy--; n++;
        if(ox == x && oy == y)
            return n;

        //3rd step
        ox++; oy++; n++;
        if(ox == x && oy == y)
            return n;

        //4th step
        ox--; oy++; n++;
        if(ox == x && oy == y)
            return n;

    }

    return -1;
    
}

int main(){

    int test_cases;
    cin >> test_cases;

    for(int i = 0; i < test_cases; i++){
        int x, y;
        cin >> x; cin >> y;

        int number = nsteps(x,y);

        if(number != -1)
            cout << number << endl;
        else 
            cout << "No Number" << endl;
    }

    return 0;
}