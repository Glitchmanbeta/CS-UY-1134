public class Sorts{
	int[] ary;

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
		int[] ary = {6, 5, 3, 1, 8, 7, 2, 4};
		Sorts s = new Sorts(ary);
		s.bubbleSort();
		System.out.println(s.toString());
	}
}