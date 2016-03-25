#include <string>
#include <iostream>
#include <cstdlib>

using namespace std;

int ascii(char a){
	int initial, fixed;
	initial = int(a);
	if (initial < 91)
		fixed = (initial - 65);
	else if (initial > 91)
		fixed = (initial - 97);

	return fixed;
}

char inv_ascii(int a){
	char final;
	final = char((a%26)+97);
	return final;

}


int main(){
	string pre;

	cin>>pre;

	char initial[pre.length()];
	int before[pre.length()];
	char final[pre.length()];

	for(int x = 0; x < pre.length(); x++){
		initial[x] = pre[x];
		before[x] = ascii(initial[x]);
		final[x] = inv_ascii(before[x]+26);
		cout<<initial[x]<<"    "<<before[x]<<"   "<<final[x]<<endl;
	}

	string post(final);

	cout<<post<<endl;

	return 0;
}
