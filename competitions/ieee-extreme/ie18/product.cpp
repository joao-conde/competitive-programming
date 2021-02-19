#include <bits/stdc++.h>
using namespace std;

int kadane(int* arr, int* start, int* finish, int n){
    int sum = 0, maxSum = INT_MIN, i;
    *finish = -1;

    int local_start = 0;
    for (i = 0; i < n; ++i){
        sum += arr[i];
        if (sum < 0){
            sum = 0;
            local_start = i+1;
        }
        else if (sum > maxSum){
            maxSum = sum;
            *start = local_start;
            *finish = i;
        }
    }

    if (*finish != -1)
        return maxSum;

    maxSum = arr[0];
    *start = *finish = 0;

    for (i = 1; i < n; i++){
        if (arr[i] > maxSum){
            maxSum = arr[i];
            *start = *finish = i;
        }
    }
    return maxSum;
}

int main(){

    int n, m; cin >> n >> m;
    int a[n], b[m];
    int sum1 = 0, sum2 = 0;

    for(int i = 0; i < n; i++){
        cin >> a[i];
        sum1 += a[i];
    }

    for(int i = 0; i < m; i++){
        cin >> b[i];
        sum2 += b[i];
    }

    int start, finish;
    int kd1 = kadane(a, &start, &finish, n),
        kd2 = kadane(b, &start, &finish, m);

    int rev_kd1 = sum1 - kd1,
        rev_kd2 = sum2 - kd2;

    cout << max(kd1 * kd2, rev_kd1 * rev_kd2) << endl;
}
