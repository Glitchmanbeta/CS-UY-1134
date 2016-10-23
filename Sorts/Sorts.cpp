#include <iostream>
#include <string>
using namespace std;
bool bubble = false;
bool selection = false;
bool insertion = true;
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

	int* selectionSort(){
		int a = 0;
		while(a < length){
			int min = ary[a];
			int index = a;
			for(int j = a; j < length; j++){
				if(ary[j] < min){
					min = ary[j];
					index = j;
				}
			}
			ary[index] = ary[a];
			ary[a] = min;
			a++;
		}
		return ary;
	}

	int* insertionSort(){
		int a = 0;
		while(a < length){
			int j = a;
			int temp = ary[a];
			while(j > 0 && ary[j - 1] > temp){
				ary[j] = ary[j - 1];
				j--;
			}
			ary[j] = temp;
			a++;
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
	int ary1[] = {1, 2, 3, 4, 5, 6, 7, 8};
	int ary2[] = {6, 5, 3, 1, 8, 7, 2, 4};
	int ary3[] = {8, 7, 6, 5, 4, 3, 2, 1};
	Sorts b(ary1, 8);
	Sorts a(ary2, 8);
	Sorts w(ary3, 8);
	cout << "C++\n";
	cout << "Best Case: " + b.toString() + "\n";
	cout << "Average Case: " + a.toString() + "\n";
	cout << "Worst Case: " + w.toString() + "\n";
	if(bubble){
		b.bubbleSort();
		a.bubbleSort();
		w.bubbleSort();
	}
	if(selection){
		b.selectionSort();
		a.selectionSort();
		w.selectionSort();
	}
	if(insertion){
		b.insertionSort();
		a.insertionSort();
		w.insertionSort();
	}
	cout << "Best Case: " + b.toString() + "\n";
	cout << "Average Case: " + a.toString() + "\n";
	cout << "Worst Case: " + w.toString() + "\n";
}