import functools
import math
import random
from time import perf_counter as pc
import concurrent.futures as future

#lst = [-1,2,3]
#f = functools.reduce(lambda x,y:x+y,lst)
#print(hej)




def hypersphere(n,d):
    return len(list(filter(lambda x: x<=1,[functools.reduce(lambda x, y: x+y, lst) for lst in [[random.uniform(-1,1)**2 for _ in range(d)] for _ in range(n)]])))


def hypersphere_2(n,d):
    with future.ProcessPoolExecutor() as ex:
        n = [n for _ in range(10)]
        d = [d for _ in range(10)]
        lst = (ex.map(hypersphere, n,d))
    return sum(lst)

def main():
    n = 100000
    d = 11
    Vd = (math.pi**(d/2))/(math.gamma((d/2)+1))
    print('Real V: ',Vd)

    start = pc()
    ns = hypersphere(n,d)
    end = pc()
    print('Normal approx time: ',end-start)
    Vapprox = (2**d*ns)/n
    print('Approx V: ',Vapprox)

    start = pc()
    ns = hypersphere_2(int(n/10),d)
    end = pc()
    print('Multiprocess approx time: ',end-start)
    Vapprox = (2**d*ns)/n
    print('Multithreadapprox V: ',Vapprox)
    pass

if __name__ == '__main__':
    main()
