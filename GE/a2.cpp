#include <iostream>
#include <string>
#include <cmath>
#include <cstdlib>

using namespace std;

string encrypt(string phrase, int seed);
string decrypt(string phrase, int seed);
int ascii(char a);
char inv_ascii(int a);


int main(){
	int seed;
	string phrase;
	char mode;

	//ask the user for the seed value,
	//if they want to encrypt/decrypt,
	//and the message to change
	cout<<"Input the seed value: ";
	cin>>seed;
	cout<<"Would you like to encrypt (e) or decrypt (d)? ";
	cin>>mode;
	cout<<"Input the phrase"<<endl;
	cin>>phrase;

	//Check if the user wants encryption or decryption
	//and modify the function used based on this
	if(mode == 'e' || mode == 'E'){
		encrypt(phrase, seed);
	}
	else if(mode == 'd' || mode == 'D'){
		decrypt(phrase, seed);
	}
	else{
		cout<<"input not recognized"<<endl;
		return 0;
	}

	
	return 0;
}



string encrypt(string phrase, int seed){
	int preshift[phrase.length()];
	int postshift[phrase.length()];

	srand(seed);

	//create a character array with length equal to the string
	char initial[phrase.length()];
	char final[phrase.length()];

	//fill the array with the characters 
	for(int x = 0; x < phrase.length(); x++){
		initial[x] = phrase[x];
	}

	//convert the letters to numbers
	//shift them based on the random number seed
	//convert that back to a letter
	for(int n = 0; n < phrase.length(); n++){
		preshift[n] = ascii(initial[n]);
		postshift[n] = preshift[n] + (rand()%26);
		final[n] = inv_ascii(postshift[n]);
	}

	//compile the individual letters into a string
	string encrypted(final);

	//print the new encrypted message and return the value
	cout << "The encrypted message is " << encrypted << endl;
	return encrypted;
}



string decrypt(string phrase, int seed){
	int preshift[phrase.length()];
	int postshift[phrase.length()];

	srand(seed);

	//create a character array with length equal to the string
	char initial[phrase.length()];
	char final[phrase.length()];

	//fill the array with the characters 
	for(int x = 0; x < phrase.length(); x++){
		initial[x] = phrase[x];
	}

	//convert to ascii characters, perform the shift back,
	//then convert back to English characters
	//ensure the ascii code is above 0 before converting
	for(int n = 0; n < phrase.length(); n++){
		preshift[n] = ascii(initial[n]);
		postshift[n] = preshift[n] - (rand()%26);
		while(postshift[n] < 0)
			postshift[n] += 26;
		final[n] = inv_ascii(postshift[n]);
	}

	string decrypted(final);

	cout << "The decrypted message is " << decrypted << endl;
	return decrypted;
}


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