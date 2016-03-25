#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int main(){
	ofstream out_file;

	out_file.open("files.txt");

	int fibonacci[20];
	fibonacci[0] = 1;
	fibonacci[1] = 1;

	for(int i = 2; i < 20; i++){
		fibonacci[i] = fibonacci[i-1]+fibonacci[i-2];
	}

	for(int i = 0; i < 20; i++){
		out_file << fibonacci[i] << endl;
	}


}