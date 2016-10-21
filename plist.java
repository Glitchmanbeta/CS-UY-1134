public class Plist{
	private Node head;
	private Node tail;
	private int size;
	private class Node<T>{
		private T data;
		private Node prev;
		private Node next;
		public Node(T data, Node prev, Node next){
			this.data = data;
			this.prev = prev;
			this.next = next;
		}
		public T data(){
			return data;
		}
		public 
	}
	private class Position<T>{
		private PList plist;
		private Node node;
		public Position(PList plist, Node node){
			this.plist = plist;
			this.node = node;
		}
		public T data(){
			return node.data();
		}
	}
	private Position make_position(Node node){
		if(node == head or node == tail){
			return null;
		}
		else{
			p = new Position(this, node);
			return p;
		}
	}
	public PList(){
		head = new Node(null, null, null);

	}
}