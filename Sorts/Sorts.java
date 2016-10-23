public class Sorts{
	private int[] ary;
	public static boolean bubble = false;
	public static boolean selection = false;
	public static boolean insertion = true;

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
		int[] ary1 = {1, 2, 3, 4, 5, 6, 7, 8};
		int[] ary2 = {6, 5, 3, 1, 8, 7, 2, 4};
		int[] ary3 = {8, 7, 6, 5, 4, 3, 2, 1};
		Sorts b = new Sorts(ary1);
		Sorts a = new Sorts(ary2);
		Sorts w = new Sorts(ary3);
		System.out.println("Java");
		System.out.println("Best Case: " + b.toString());
		System.out.println("Average Case: " + a.toString());
		System.out.println("Worst Case: " + w.toString());
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
		System.out.println("Best Case: " + b.toString());
		System.out.println("Average Case: " + a.toString());
		System.out.println("Worst Case: " + w.toString());
	}
}