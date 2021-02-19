//https://www.spoj.com/problems/PIE/

#include <bits/stdc++.h>
using namespace std;

#define MAX_SLICE_VOLUME 315000000

bool isSolution(double sliceV, vector<double> piesV, int friends){

    int slices = 0;
    for(int i = 0; i < piesV.size(); i++)
        slices += (int)(piesV[i] / sliceV);

    return (slices >= friends);
}

int main(){

    ios::sync_with_stdio(0);
    cin.tie();

    double pi = acos(-1.0);

    int testCases; cin >> testCases;
    while(testCases--){

        int npies, friends;
        cin >> npies >> friends;

        vector<double> pieVolumes;
        for(int i = 0; i < npies; i++){
            double pieRadii; cin >> pieRadii;
            pieVolumes.push_back(pieRadii*pieRadii*pi);
        }


        double lb = 0, ub = MAX_SLICE_VOLUME, mid;
        while(ub - lb > 0.00001){

            mid = (lb + ub) / 2;

            if(isSolution(mid, pieVolumes, friends + 1)){
                lb = mid;
            }
            else{
                ub = mid;
            }

        }

        printf("%.4f\n", lb);

    }

}
