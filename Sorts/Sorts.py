import random
import sys
class Sorts:

	def __init__(self, ary):
		self._ary = ary

	def bogoSort(self):
		sorted = False
		while not sorted:
			i = 0
			while self._ary[i] < self._ary[i + 1]:
				if i == len(self._ary) - 2:
					if self._ary[i] < self._ary[i + 1]:
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

	def quickSortHelp(self, pivot, left, right):
		l = left
		r = right
		if left > right:
			return self._ary
		if pivot == 1:
			if self._ary[0] > self._ary[1]:
				temp = self._ary[0]
				self._ary[0] = self._ary[1]
				self._ary[1] = temp
			return self._ary
		elif pivot == 0:
			return self._ary
		else:
			while l != r and l < r:
				if self._ary[l] > self._ary[pivot] and self._ary[r] < self._ary[pivot]:
					temp = self._ary[l]
					self._ary[l] = self._ary[r]
					self._ary[r] = temp
					l += 1
					r -= 1
				elif self._ary[l] > self._ary[pivot] and self._ary[r] > self._ary[pivot]:
					r -= 1
				elif self._ary[l] < self._ary[pivot] and self._ary[r] < self._ary[pivot]:
					l += 1
				else:
					l += 1
					r -= 1
			if self._ary[l] < self._ary[pivot]:
				l += 1
			temp = self._ary[l]
			self._ary[l] = self._ary[pivot]
			self._ary[pivot] = temp
			self.quickSortHelp(l - 1, left, l - 2)
			self.quickSortHelp(len(self._ary) - 1, l + 1, right)
		return self._ary

	def quickSort(self):
		return self.quickSortHelp(len(self._ary) // 2, 0, len(self._ary) - 1)

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
	ary1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
	ary2 = [9, 20, 29, 40, 49, 60, 69, 80, 89, 100, 6, 15, 23, 31, 48, 57, 62, 74, 86, 95, 5, 13, 21, 38, 47, 52, 64, 76, 85, 93, 3, 11, 28, 37, 42, 54, 66, 75, 83, 91, 1, 18, 27, 32, 44, 56, 65, 73, 81, 98, 8, 17, 22, 34, 46, 55, 63, 71, 88, 97, 7, 12, 24, 36, 45, 53, 61, 78, 87, 92, 2, 14, 26, 35, 43, 51, 68, 77, 82, 94, 4, 16, 25, 33, 41, 58, 67, 72, 84, 96, 10, 19, 30, 39, 50, 59, 70, 79, 90, 99]
	ary3 = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
	b = Sorts(ary1)
	a = Sorts(ary2)
	w = Sorts(ary3)
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
			s.bubbleSort()
			print(s.toString())
			return
		else:
			raise IndexError()
	except IndexError:
		print("Please indicate which sort you would like to run by typing 'python3 Sorts.py <X>Sort', where X is the name of the sort")

main()