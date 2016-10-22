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
		return self._ary

def main():
	ary = [6, 5, 3, 1, 8, 7, 2, 4]
	s = Sorts(ary)
	print(s.toString())
	s.bubbleSort()
	print(s.toString())
	ary = [6, 5, 3, 1, 8, 7, 2, 4]
	s = Sorts(ary)
	s.selectionSort()
	print(s.toString())

main()