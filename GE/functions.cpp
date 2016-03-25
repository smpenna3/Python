#include <iostream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;

int factorial(int n);
float distance(float x, float y);

int main(){
	cout<<factorial(3)<<endl;

	
	return 0;
}


int factorial(int n){
	int result = 1;
	for(int x = 1; x <= n; x++){
		result *= x;
	}

	return result;
}
