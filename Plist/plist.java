public class LinkedList<T>{
	private class Node<T>{
		private T data;
		private Node prev;
		private Node next;
		public Node(Node prev, T data, Node next){
			this.prev = prev;
			this.data = data;
			this.next = next;
		}
		public Node getPrev(){
			return prev;
		}
		public Node getNext(){
			return next;
		}
		public T data(){
			return data;
		}
		public void setData(T data){
			this.data = data;
		}
		public void setPrev(Node prev){
			this.prev = prev;
		}
		public void setNext(Node next){
			this.next = next;
		}
	}
	private Node head;
	private Node tail;
	private int size;
	public LinkedList(){
		head = new Node(null, null, null);
		tail = head;
	}
	public int size(){
		return size;
	}
	public T data(int p){
		if(p >= size){
			throw new IndexOutOfBoundsException();
		}
		else{
			Node current;
			if(p > size / 2){
				current = tail;
				for(i = size; i != p; i--){
					current = current.getPrev();
				}
				return current;
			}
			else{
				current = head;
				for(i = 0; i != p; i++){
					current = current.getNext();
				}
				return current;
			}
		}
	}
	public void 
}