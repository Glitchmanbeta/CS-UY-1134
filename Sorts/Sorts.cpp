#include <iostream>
#include <string>
#include <sstream>
using namespace std;
bool bubble = false;
bool selection = false;
bool insertion = false;
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

	int* quickSort(){
		return quickSortHelp(0, length - 1);
	}

	int* quickSortHelp(int left, int right){
		if(left == right || left > right){
			return ary;
		}
		else if(left + 1 == right){
			if(ary[left] > ary[right]){
				int temp = ary[left];
				ary[left] = ary[right];
				ary[right] = temp;
				return ary;
			}
		}
		else{
			int pivot = right;
			int l = left;
			int r = right - 1;
			while(l < r){
				if(ary[l] <= ary[pivot] && ary[r] > ary[pivot]){
					l++;
					r--;
				}
				else if(ary[l] <= ary[pivot] && ary[r] <= ary[pivot]){
					l++;
				}
				else if(ary[l] > ary[pivot] && ary[r] > ary[pivot]){
					r--;
				}
				else if(ary[l] > ary[pivot] && ary[r] <= ary[pivot]){
					int temp = ary[l];
					ary[l] = ary[r];
					ary[r] = temp;
					l++;
					r--;
				}
			}
			if(ary[l] < ary[pivot]){
				l++;
			}
			int temp = ary[l];
			ary[l] = ary[pivot];
			ary[pivot] = temp;
			quickSortHelp(left, l - 1);
			quickSortHelp(l + 1, right);
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

int main(int argc, char *argv[]){
	int ary0[] = {6, 5, 3, 1, 8, 7, 2, 4};
	Sorts s(ary0, 8);
	stringstream ss;
	string str;
	ss << argv[1];
	ss >> str;
	try{
		if(str.compare("BubbleSort") == 0){
			cout << "C++ Bubble Sort\n";
			cout << s.toString() + "\n";
			s.bubbleSort();
			cout << s.toString() + "\n";
		}
		else if(str.compare("SelectionSort") == 0){
			cout << "C++ Selection Sort\n";
			cout << s.toString() + "\n";
			s.selectionSort();
			cout << s.toString() + "\n";
		}
		else if(str.compare("InsertionSort") == 0){
			cout << "C++ Insertion Sort\n";
			cout << s.toString() + "\n";
			s.insertionSort();
			cout << s.toString() + "\n";
		}
		else if(str.compare("QuickSort") == 0){
			cout << "C++ Quick Sort\n";
			cout << s.toString() + "\n";
			s.quickSort();
			cout << s.toString() + "\n";
		}
		else{
			throw 69;
		}
	}
	catch(int e){
		cout << "Please indicate which sort you would like to run by typing './Sorts <X>Sort', where X is the name of the sort\n";
	}
}