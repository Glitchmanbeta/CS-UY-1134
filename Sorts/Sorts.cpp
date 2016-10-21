#include <iostream>
#include <string>
using namespace std;

void bubbleSort(int ary[]){
	int a = ary.length;
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
	for(int i = 0; i < ary.length; i++){
		if(i == ary.length - 1){
			s += ary[i] + "]";
		}
		else{
			s += ary[i] + ", ";
		}
	}
	return s;
}
