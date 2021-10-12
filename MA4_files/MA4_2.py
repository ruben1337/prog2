#!/usr/bin/env python3

from integer import Integer
from time import perf_counter as pc
import matplotlib.pyplot as plt

def fib_py(n):
	if(n<=1):
		return n
	return fib_py(n-1) + fib_py(n-2)

def main():
	#n = 31
	#for n in range(30,46):

	#	start = pc()
	#	fib_py(n)
	#	end = pc()
	#	print(n,end-start)
	timeP=[0.28, 0.44, 0.71, 1.15, 1.86, 3.00, 4.88, 7.90, 12.83, 20.67, 33.62, 53.97, 89.22, 142,59, 232.51, 376.80]

	timeC=[]
	nlist = [n for n in range(30,46)]
	for n in nlist:
		start = pc()
		f = Integer(n)
		f.fib()
		end = pc()
		timeC.append(end-start)
	plt.plot(nlist,timeP)
	plt.plot(nlist,timeC)
	plt.xlabel('n')
	plt.ylabel('time [s]')
	plt.savefig('MA4plot.png')

if __name__ == '__main__':
	main()