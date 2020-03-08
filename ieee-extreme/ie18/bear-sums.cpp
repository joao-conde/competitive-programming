/*
Time limit: 9000 ms
Memory limit: 256 MB

Mitsos the bear is challenging his brother Vangelis with a mathematical task. Mitsos provides a list of 
integers L and another integer value S, then he asks Vangelis to check if there are any two items in 
the list L whose sum is equal to the integer S.

Since Vangelis is a confident engineer, he decided to write a program that would do all the computations
for him and skip the trouble of thinking. Your task is to help Vangelis write a program that reads the 
input list L and the integer S and produces either the solution to the problem or provides an error 
message when there is no solution available.

--Standard input--

On the first line there will be an integer number T (representing the number of test cases) followed by 
2 input lines for each test case:

    * On the first line of each test case, there will be 2 integers S and E, where S is the expected sum 
    and E is the number of elements in the list.
    
    * On the second line, there will be E integers separated by a space. Each integer represents an element
    of the list L. The elements are not sorted in any way and some could have the same value. In cases where 
    the number E is 000, the second line will be empty. 

All values for the elements of list L will be in the same range as the value S.

--Standard output--

For each test case you will have to write one line that contains:

    * If there is an unique solution: Write two elements, x and y of the list L, separated by a single 
    space, such that x + y = S and x <= y.
    * If there are multiple solutions: pick the first complete pair that appears on the list and provides 
    the correct sum. Print the two list elements forming this pair in increasing order.
    * If there is no solution: Print the error message !OK. 

--Constraints and notes--

    * 1 <= T <= 1000
    * −10⁶ < S < 10⁶ ​​
    * 0 <= E <= 2⋅10⁴​​
    * The sum of values of E is at most 10⁷​​ 
*/

#include <bits/stdc++.h>
using namespace std;

#define INF 100000000

int main(){

    int t; cin >> t;
    while(t--){
        int s, e;
        cin >> s >> e;

        //value, smallest index and frequency
        unordered_map<int, pair<int,int>> table;
        vector<int> items;
        for(int i = 0; i < e; i++){
            int item; cin >> item;
            items.push_back(item);

            unordered_map<int, pair<int,int>>::iterator it = table.find(item);
            if(it == table.end()){
                table.insert({item, {i, 1}});
            }
            else{
                if(table[item].first < i) table[item].first = i;
                table[item].second++;
            }

        }
        
        map<int, pair<int,int>> pairs;
        for(int i = 0; i < items.size(); i++){
            int complement = s - items.at(i);
            unordered_map<int, pair<int,int> >::iterator it = table.find(complement);
            if(it != table.end()){
                if(items.at(i) == complement)
                    if(it->second.second <= 1)
                        continue;
                
                int index2 = it->second.first;
                pair<int, int> pair_el = make_pair(min(complement, items.at(i)), max(complement, items.at(i)));
                pairs.insert({max(i, index2), pair_el});
                
            }
        }

       
        if(pairs.size() == 0) 
            cout << "!OK\n";
        else{
            pair<int, int> pair_sol;
            int index = INF;

            for(auto el: pairs){
                if(el.first < index){
                    index = el.first;
                    pair_sol = el.second;
                }
            }

            cout << pair_sol.first << " " << pair_sol.second << endl;  
        }
    }


}