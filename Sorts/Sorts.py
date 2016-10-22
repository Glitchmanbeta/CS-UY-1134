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

	def toString(self):
		return self._ary

def main():
	ary = [6, 5, 3, 1, 8, 7, 2, 4]
	s = Sorts(ary)
	s.bubbleSort()
	print(s.toString())

main()