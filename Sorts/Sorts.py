bubble = False
selection = True
class Sorts:

	def __init__(self, ary):
		self._ary = ary

	def bubbleSort(self):
		a = len(self._ary)
		while a > 0:
			for j in range(a - 1):
				if self._ary[j] > self._ary[j + 1]:
					temp = self._ary[j]
					self._ary[j] = self._ary[j + 1]
					self._ary[j + 1] = temp
			a -= 1
		return self._ary

	def selectionSort(self):
		a = 0
		while a < len(self._ary):
			min = self._ary[a]
			index = a
			for j in range(a, len(self._ary)):
				if self._ary[j] < min:
					min = self._ary[j]
					index = j
			self._ary[index] = self._ary[a]
			self._ary[a] = min
			a += 1
		return self._ary

	def toString(self):
		s = "["
		for i in range(len(self._ary)):
			if i == len(self._ary) - 1:
				s += str(self._ary[i]) + "]"
			else:
				s += str(self._ary[i]) + ", "
		return s

def main():
	ary1 = [1, 2, 3, 4, 5, 6, 7, 8]
	ary2 = [6, 5, 3, 1, 8, 7, 2, 4]
	ary3 = [8, 7, 6, 5, 4, 3, 2, 1]
	b = Sorts(ary1)
	a = Sorts(ary2)
	w = Sorts(ary3)
	print("Python")
	print("Best Case: " + b.toString())
	print("Average Case: " + a.toString())
	print("Worst Case: " + w.toString())
	if bubble:
		b.bubbleSort()
		a.bubbleSort()
		w.bubbleSort()
	if selection:
		b.selectionSort()
		a.selectionSort()
		w.selectionSort()
	print("Best Case: " + b.toString())
	print("Average Case " + a.toString())
	print("Worst Case " + w.toString())

main()