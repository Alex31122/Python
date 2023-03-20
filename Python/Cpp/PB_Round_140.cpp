#include <iostream>
#include <algorithm>

using namespace std;

int main(){

    int i,t,N1;
    int Array[1000];

    cin >> t;
    cin >> N1;

    for(i=0;i<t-1;i++){
        cin >> Array[i];
    }
    sort(Array[0],Array[5]);

    for(i=0;i<t-1;i++){
        cout << Array[i];
    }

    cout << endl << endl;
    return 0;
}
