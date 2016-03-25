#include <iostream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;

float max(float a, float b);

int main(){
	string c;

	cin>>c;

	cout<<max(4, 3);

	return 0;
}


float max(float a, float b){
	if((a>b)){
		return a;
	}

	else if ((a<b)){
		return a;
	}

	else{
		return b;
	}

}