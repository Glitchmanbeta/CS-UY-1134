import random
import sys
class Heap:

	def __init__(self):
		_A = []

	def add(self, i):
		_A.append
class Sorts:

	def __init__(self, ary):
		self._ary = ary

	def bogoSort(self):
		sorted = False
		if len(self._ary) <= 1:
			return self._ary
		while not sorted:
			i = 0
			while self._ary[i] <= self._ary[i + 1]:
				if i == len(self._ary) - 2:
					if self._ary[i] <= self._ary[i + 1]:
						return self._ary
				i += 1
			random.shuffle(self._ary)

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

	def insertionSort(self):
		a = 0
		while a < len(self._ary):
			j = a
			temp = self._ary[a]
			while j > 0 and self._ary[j - 1] > temp:
				self._ary[j] = self._ary[j - 1]
				j -= 1
			self._ary[j] = temp
			a += 1
		return self._ary

	def quickSort(self):
		return self._quickSortHelp(0, len(self._ary) - 1)

	def _quickSortHelp(self, left, right):
		if left == right or left > right:
			return self._ary
		elif left + 1 == right:
			if self._ary[left] > self._ary[right]:
				temp = self._ary[left]
				self._ary[left] = self._ary[right]
				self._ary[right] = temp
				return self._ary
		else:
			pivot = right
			l = left
			r = right - 1
			while l < r:
				if self._ary[l] <= self._ary[pivot] and self._ary[r] > self._ary[pivot]:
					l += 1
					r -= 1
				elif self._ary[l] <= self._ary[pivot] and self._ary[r] <= self._ary[pivot]:
					l += 1
				elif self._ary[l] > self._ary[pivot] and self._ary[r] > self._ary[pivot]:
					r -= 1
				elif self._ary[l] > self._ary[pivot] and self._ary[r] <= self._ary[pivot]:
					temp = self._ary[l]
					self._ary[l] = self._ary[r]
					self._ary[r] = temp
					l += 1
					r -= 1
			if self._ary[l] < self._ary[pivot]:
				l += 1
			temp = self._ary[l]
			self._ary[l] = self._ary[pivot]
			self._ary[pivot] = temp
			self._quickSortHelp(left, l - 1)
			self._quickSortHelp(l + 1, right)

	def mergeSort(self):
		if len(self._ary) == 0 or len(self._ary) == 1:
			return self._ary
		else:
			self._ary = self._mergeSortHelp(self._ary)

	def _mergeSortHelp(self, ary):
		if len(ary) <= 1:
			return ary
		else:
			ary1 = []
			ary2 = []
			for i in range(len(ary)):
				if i < len(ary) // 2:
					ary1.append(ary[i])
				else:
					ary2.append(ary[i])
			ary1 = self._mergeSortHelp(ary1)
			ary2 = self._mergeSortHelp(ary2)
			return self._merge(ary1, ary2)

	def _merge(self, ary1, ary2):
		l = 0
		r = 0
		i = 0
		merged = []
		while l < len(ary1) and r < len(ary2):
			if ary1[l] <= ary2[r]:
				merged.append(ary1[l])
				l += 1
				i += 1
			elif ary2[r] <= ary1[l]:
				merged.append(ary2[r])
				r += 1
				i += 1
		while l < len(ary1):
			merged.append(ary1[l])
			i += 1
			l += 1
		while r < len(ary2):
			merged.append(ary2[r])
			i += 1
			r += 1
		return merged

	def radixSort(self):
		raise NotImplementedError("This operation is currently unsupported")

	def toString(self):
		s = "["
		for i in range(len(self._ary)):
			if i == len(self._ary) - 1:
				s += str(self._ary[i]) + "]"
			else:
				s += str(self._ary[i]) + ", "
		return s

def main():
	ary0 = [6, 5, 3, 1, 8, 7, 2, 4]
	"""ary0 = []
	for i in range(int(sys.argv[2])):
		ary0.append(random.randint(0, i))"""
	s = Sorts(ary0)
	try:
		if sys.argv[1] == "BogoSort":
			print("Python Bogo Sort")
			print(s.toString())
			s.bogoSort()
			print(s.toString())
			return
		elif sys.argv[1] == "BubbleSort":
			print("Python Bubble Sort")
			print(s.toString())
			s.bubbleSort()
			print(s.toString())
			return
		elif sys.argv[1] == "SelectionSort":
			print("Python Selection Sort")
			print(s.toString())
			s.selectionSort()
			print(s.toString())
			return
		elif sys.argv[1] == "InsertionSort":
			print("Python Insertion Sort")
			print(s.toString())
			s.insertionSort()
			print(s.toString())
			return
		elif sys.argv[1] == "QuickSort":
			print("Python Quick Sort")
			print(s.toString())
			s.quickSort()
			print(s.toString())
			return
		elif sys.argv[1] == "MergeSort":
			print("Python Merge Sort")
			print(s.toString())
			s.mergeSort()
			print(s.toString())
		else:
			raise IndexError()
	except IndexError:
		print("Please indicate which sort you would like to run by typing 'python3 Sorts.py <X>Sort', where X is the name of the sort")

main()