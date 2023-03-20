#include <iostream>

using namespace std;

int main(){
    int t,i,M;
    int nums[3];

    cin >> t;

    for(int i=0; i<3; i++){
        cin >> nums[i];
    }
    
    for(int i=0; i<3; i++){
        if(nums[i]<nums[i+1]){
            nums[i+1] = nums[i];
        }
    }

    return 0;
}