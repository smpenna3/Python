#include <iostream>


using namespace std;

int main(){
	unsigned long long current;
	int i = 0;
	cin>>current;
	
	while(current != 1){
		if((current % 2) == 0)
			current /= 2;
		else
			current = (current*3)+1;

		cout<<current<<endl;
		i++;
	}

	cout<<endl<<"it took "<<i<<" times"<<endl;

	return 0;
}