#include <bits/stdc++.h>
using namespace std;

#define MAX 100000

struct Star{
    int s, f, d;
    Star(int s, int f, int d){
        s = s; f = f; d = d;
    }
};

vector<Star> stars;

bool star_comp(Star s1, Star s2){ 
    return (s1.f < s2.f); 
} 

int main(){

    int nstars; cin >> nstars;
    for(int i = 0; i < nstars; i++){
        int si, fi, di;
        cin >> si >> fi >> di;
        stars.push_back(Star(si, fi, di));
    }

    sort(stars.begin(), stars.end(), star_comp);

    cout << compute_desirability(stars, nstars) << endl;
}