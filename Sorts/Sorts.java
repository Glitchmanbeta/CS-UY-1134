public class Sorts{
	private int[] ary;

	public Sorts(int[] ary){
		this.ary = ary;
	}

	public int[] bubbleSort(){
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

	public int[] selectionSort(){
		int a = 0;
		while(a < ary.length){
			int min = ary[a];
			int index = a;
			for(int j = a; j < ary.length; j++){
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

	public int[] insertionSort(){
		int a = 0;
		while(a < ary.length){
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

	public int[] quickSort(){
		return quickSortHelp(0, ary.length - 1);
	}

	private int[] quickSortHelp(int left, int right){
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

	public int[] mergeSort(){
		if(ary.length <= 1){
			return ary
		}
		else{
			ary = mergeSortHelp(ary)
		}
	}

	private int[] mergeSortHelp(int[] ary){
		if(ary.length <= 1){
			return ary
		}
		else{
			int[] ary = int[8]
		}
	}

	public String toString(){
		String s = "[";
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

	public static void main(String[] args){
		int[] ary0 = {6, 5, 3, 1, 8, 7, 2, 4};
		Sorts s = new Sorts(ary0);
		try{
			if(args[0].equals("BubbleSort")){
				System.out.println("Java Bubble Sort");
				System.out.println(s.toString());
				s.bubbleSort();
				System.out.println(s.toString());
			}
			else if(args[0].equals("SelectionSort")){
				System.out.println("Java Selection Sort");
				System.out.println(s.toString());
				s.selectionSort();
				System.out.println(s.toString());
			}
			else if(args[0].equals("InsertionSort")){
				System.out.println("Java Insertion Sort");
				System.out.println(s.toString());
				s.insertionSort();
				System.out.println(s.toString());
			}
			else if(args[0].equals("QuickSort")){
				System.out.println("Java Quick Sort");
				System.out.println(s.toString());
				s.quickSort();
				System.out.println(s.toString());
			}
		}
		catch (IndexOutOfBoundsException e){
			System.out.println("Please indicate which sort you would like to run by typing 'java Sorts <X>Sort', where X is the name of the sort");
		}
	}
}