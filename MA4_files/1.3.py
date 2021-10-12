from time import perf_counter as pc
from time import sleep as pause#import multiprocessing as mpimport concurrent.futures as futuredef runner(n):
    print(f"Performing costly function {n}")
    pause(n)
    return f"Function {n} has completed"

if __name__ == "__main__":
    start = pc()

    with future.ThreadPoolExecutor() as ex:
        p = [1,2,3,4,5]
        results = ex.map(runner, p)

        for r in results:
            print(r)

    end = pc()
    print(f"Process took {round(end-start, 2)} seconds")