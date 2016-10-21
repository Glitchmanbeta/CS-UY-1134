import timeit
import turtle

def timeFunction(f, n, repeat = 1):
	return timeit.timeit(f.__name__+ '(' + str(n) + ')',
		setup = "from __main__ import " + f.__name__, number = repeat)/repeat

#Task 1
def fib1(n):
	if n == 0:
		return 0
	if n == 1 or n == 2:
		return 1
	else:
		return fib1(n - 1) + fib1(n - 2)

#Task 2
def fib2(n):
	A = [0]
	if n > 0:
		A.append(1)
	if n > 1:
		A.append(1)
	for i in range(3, n + 1):
		A.append(A[-1] + A[-2])
	return A[-1]

#Task 3
def fib3(n):
	a = 0
	b = 1
	if n == 0:
		return a
	elif n == 1:
		return b
	for i in range(2, n + 1):
		a, b = b, a + b
	return b

#Task 4
def printFunctionTimes(func, n):
	for x in n:
		for f in func:
			s = "n = " + str(x) + ":" + f.__name__ + ":" + str("{:4.6f}".format(timeFunction(f, x)))
			print(s)

#Task 5
def plotFunctionTimesSimple():
	for n in range(1, 300):
		turtle.goto(n, timeFunction(fib2, n, 100) * 500000)

def plotFunctionTimes(functions, colors, xrange, maxy, repeat = 1):
	D = {}
	turtle.setworldcoordinates(0, 0, xrange[-1], maxy)
	for x, y in zip(functions, colors):
		D[y] = turtle.Turtle()
		D[y].pencolor(y)
	for z in xrange:
		for x, y in zip(functions, colors):
			D[y].goto(z, timeFunction(x, z, repeat))


def main():
	#for f in (fib1, fib2, fib3):
		#print([f(i) for i in range(10)])
	#printFunctionTimes((fib1, fib2, fib3), range(5, 40, 5))
	#plotFunctionTimesSimple()
	plotFunctionTimes((fib2, fib3), ("black", "red"), range(1, 1000, 2), 0.001, repeat = 10)

main()