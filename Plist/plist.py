class PList:
    class _Node:
        __slots__='_data','_prev','_next'
        def __init__(self,data,prev,next):
            self._data=data
            self._prev=prev
            self._next=next
    class Position:
        def __init__(self,plist,node):
            self._plist=plist
            self._node=node
        def data(self):
            return self._node._data
        def __eq__(self,other):
            return type(other) is type(self) and other._node is self._node
        def __ne__(self,other):
            return not (self == other)
    def _validate(self,p):
        if not isinstance(p,self.Position):
            raise TypeError("p mist be proper Position type")
        if p._plist is not self:
            raise ValueError('p does not belong to this PList')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node
    def _make_position(self,node):
        if node is self._head or node is self._tail:
            return None
        else:
            return self.Position(self,node)
    def __init__(self):
        self._head=self._Node(None,None,None)
        self._head._next=self._tail=self._Node(None,self._head,None)
        self._size=0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size==0
    def first(self):
        return self._make_position(self._head._next)
    def last(self):
        return self._make_position(self._tail._prev)
    def before(self,p):
        node=self._validate(p)
        return self._make_position(node._prev)
    def after(self,p):
        node=self._validate(p)
        return self._make_position(node._next)
    def __iter__(self):
        pos = self.first()
        while pos:
            yield pos.data()
            pos=self.after(pos)
    def _insert_after(self,data,node):
        newNode=self._Node(data,node,node._next)
        node._next._prev=newNode
        node._next=newNode
        self._size+=1
        return self._make_position(newNode)
    def add_first(self,data):
        return self._insert_after(data,self._head)
    def add_last(self,data):
        return self._insert_after(data,self._tail._prev)
    def add_before(self,p,data):
        node=self._validate(p)
        return self._insert_after(data,node._prev)
    def add_after(self,p,data):
        node=self._validate(p)
        return self._insert_after(data,node)
    def delete(self,p):
        node=self._validate(p)
        data=node._data
        node._prev._next=node._next
        node._next._prev=node._prev
        node._prev=node._next=node._data=None
        self._size-=1
        return data
    def replace(self,p,data):
        node=self._valdiate(p)
        olddata=node._data
        node._data=data
        return olddata
    def rev_itr(self):
        pos = self.last()
        while pos:
            yield pos.data()
            pos=self.before(pos)




class Topk:
    class Counter:
        def __init__(self,name,pos):
            self._name=name
            self._count=0
            self._pos=pos
        def count(self):
            return self._count
        def name(self):
            return self._name
    def __init__(self):
        self._L=PList()
    def newCounter(self,name):
        counter=self.Counter(name,None)
        pos=self._L.add_last(counter)
        counter._pos=pos
        return counter
    def increment(self,counter):
        counter._count+=1
        while (self._L.before(counter._pos)
                and self._L.before(counter._pos).data().count()<counter._count):
            b=self._L.before(counter._pos)
            newpos=self._L.add_before(b,counter)
            self._L.delete(counter._pos)
            counter._pos=newpos
    def topk(self,k):
        pos = self._L.first()
        for i in range(k):
            yield pos.data()
            pos=self._L.after(pos)


import random

T=Topk()
counters=[]
for i in ("a","b","c","d","e","f","g","h","i","j"):
    counters.append(T.newCounter(i))
print("All zero")
print([(c.name(),c.count()) for c in T.topk(5)])
T.increment(counters[1])
print("Increment b")
print([(c.name(),c.count()) for c in T.topk(5)])
T.increment(counters[8])
T.increment(counters[8])
print("Increment i twice")
print([(c.name(),c.count()) for c in T.topk(5)])
for i in range(1000):
    T.increment(counters[random.randrange(10)])
print("Lots of random increments")
print([(c.name(),c.count()) for c in T.topk(10)])