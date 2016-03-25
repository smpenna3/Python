#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int main(){
	int radius = 0, area = 0, x, y;
	float pi_guess = 0, distance = 0;
	cin>>radius;

	for(y = 0; y <= radius; y++){
		for(x = 0; x <= radius; x++){
			distance = sqrt(x*x+y*y);
			if(distance <= radius){
				area++;
			}
		}
	}

	cout<<"area "<<area<<endl<<"radius "<<radius<<endl;
	area = area*4.00;
	area -= 3*radius;
	cout<<fixed<<setprecision(10)<<"Pi estimate is "<<(area/pow(radius,2))<<endl;
	return 0;
}