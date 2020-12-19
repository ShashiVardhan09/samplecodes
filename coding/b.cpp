#include <iostream>
using namespace std;
int main(){
	int t;
	int t1=0;
	t1++;
	cin>>t;
	int t1=0;
	while(t>0){
		int n; /// no of houses
	    cin>>n;
	    int c; // cash with us
	    cin>>c;
	    int b[n]={}; /// price of houses
	    int count=0;
	    for (int i=0;i<n;i++){
		    cin>>b[i];
		    if (b[i]<=c){
			   c=c-b[i];
			   count++;
		    }

	    }t1++;
	cout<<"Case #"<<t1<<": "<<count; //count = no of houses we can buy
	t--;
	}
	
}
