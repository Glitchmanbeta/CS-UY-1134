#include <iostream>
#include <string>
using namespace std;

class Sorts{
public:
	Sorts(int* yra, int size){
		ary = yra;
		length = size;
	}

	int* bubbleSort(){
		int a = length;
		while(a > 0){
			for(int j = 0; j < a - 1; j++){
				if(ary[j] > ary[j + 1]){
					int temp = ary[j];
					ary[j] = ary[j + 1];
					ary[j + 1] = temp;
				}
			}
			a--;
		}
		return ary;
	}

	string toString(){
		string s = "[";
		for(int i = 0; i < length; i++){
			if(i == length - 1){
				s += std::to_string(ary[i]) + "]";
			}
			else{
				s += std::to_string(ary[i]) + ", ";
			}
		}
		return s;
	}
private:
	int* ary;
	int length;
};

int main(){
	int ary[8] = {6, 5, 3, 1, 8, 7, 2, 4};
	Sorts s(ary, 8);
	s.bubbleSort();
	cout << s.toString();
}