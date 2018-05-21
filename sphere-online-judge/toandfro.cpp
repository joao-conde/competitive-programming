//http://www.spoj.com/problems/TOANDFRO/

#include <iostream>
#include <string>

using namespace std;

/*
*   Nao funciona mas a ideia é converter o input numa string ou array 1D e usar basicamente algo como SIZE*LINE+COL para ir ler a letra certa
*   Há claramente um padrao de leitura
*   É necessario construir a string da forma correta tho. Ou se calhar nao, tenho de pensar melhor*
*/
string rearrange(string input, int size){

    string result = "wat";
    int i = 0, flip = 0;

    while(i < input.size() - size){

        result += input[i] + input[i+1] + input[i+2];
        cout << result << endl;
        i += 3;
    }


    return result;
}

int main(){

    int size;
    string input = "", cypher;

    while(true){
        cin >> size;
        if(size == 0)
            break;

        
        cin >> input;
        
        
        
        cypher = rearrange(input, size);

        cout << "CYPHER: " << cypher << endl;
        
    }


    return 0;
}