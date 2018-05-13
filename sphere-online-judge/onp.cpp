//http://www.spoj.com/problems/ONP/

#include <stack>
#include <vector>
#include <string>
#include <map>
#include <utility>
#include <algorithm>
#include <iostream>

#define EXP_LENGTH 450

using namespace std;

string to_RPN(string str){

    string rpn = "";

    stack<char> operators;

    //operators and precedence
    map<char,int> ops;
    ops['+'] = 1;
    ops['-'] = 1;
    ops['*'] = 2;
    ops['/'] = 2;
    ops['^'] = 3;
    ops['('] = 4;
    ops[')'] = 4;


    for(int i = 0; i < str.size(); i++){
        char token = str.at(i);

        //token is an operator
        if(ops.find(token) != ops.end()){

            //special treatment for ')' token
            if(token == ')'){
                
                while(!operators.empty()){

                    if(operators.top() == '('){
                        operators.pop();
                        break;
                    }

                    rpn += operators.top();
                    operators.pop();
                }

                continue;
            }

            int p1, p2 = -1;
            p1 = ops.find(token)->second;
            if(!operators.empty()){
                p2 = ops.find(operators.top())->second;
            }

            if(p1 == p2 && token != '('){
                rpn += operators.top();
                operators.pop();
            }

            operators.push(token);
            
        }

        //token is an operand
        else rpn += token;
    }

    while(!operators.empty()){
        rpn += operators.top();
        operators.pop();
    }

    return rpn;
}

int main(){

    int test_cases;
    scanf("%d", &test_cases);

    string output = "";
    string exp;

    for(int i = 0; i < test_cases; i++){
        cin >> exp;
        output += to_RPN(exp) + '\n';
    }

    cout << output;

    return 0;
}