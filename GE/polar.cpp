#include <iostream>
#include <iomanip>
#include <string>
#include <cmath>

using namespace std;

int main(){

	double x, y, r, theta;
	cout<<"what is the value for x? ";
	cin>>x;
	cout<<"what is the value for y? ";
	cin>>y;

	r = sqrt(pow(x,2)+pow(y,2));
	theta = atan(y/x);
	theta = theta * (180/3.14159265);

	cout<< setprecision(5) << "The polar coordinate values are (" << r  << " , " << theta << ")" << endl;

	return 0;
}