//http://www.spoj.com/problems/ACPC10A/

#include <iostream>
#include <string>

using namespace std;
int main(){

    int x, y, z, n;
    string type; 

    while(true){
        cin >> x; cin >> y; cin >> z;
        n = z;

        //termination case
        if(x == 0 && y == 0 && z == 0)
            break;
   

        if(abs(x-y) == abs(y-z)){
            type = "AP";
            n += (y - x); 
        }
        else{
            type = "GP";
            n *= z/y;
        }

        cout << type << " " << n << endl;
    
    }

    return 0;
}