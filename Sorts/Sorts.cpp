#include <iostream>
#include <string>
using namespace std;

class Sorts{
public:
	Sorts(int* yra){
		ary = yra;
	}
	int* Print(){
		return ary;
	}
private:
	int* ary;
};

int main(){
	int ary[8] = {6, 5, 3, 1, 8, 7, 2, 4};
	Sorts s(ary);
	cout << s.Print();
}