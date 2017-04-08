#/usr/bin/env python3

"""Show detrement of the GIL to CPU-bound tasks

Run a CPU-bound process in the main process,
as multiple threads,
and as multiple processes

Results on Intel(R) Celeron(R) 2955U @ 1.40GHz
without powersaving scaling fussed with:
```
Native: 13.373263
Threading: 21.938521
Threading raw: 20.685542
Processing: 6.968376
Processing raw: 6.867701
```
Note: CPU ran at a lower frequency during Threading.
Interpret that as you will.

Also, this isn't overly precise
"""

import multiprocessing
import threading
import logging
import math
import time

def naive_largest_prime(nmax=10000):
    """Find the langest prime number up to nmax

    This is purposefully inefficient
    """
    if nmax <= 3:
        # Trivially low numbered prime
        return nmax
    
    best = 2
    for n in range(2,nmax+1):
        for d in range(2, nmax // 2):
            if not n % d:
                # Composite
                break
        else:
            # Prime
            best = n

    return best


if __name__ == '__main__':
    nruns = 20

    # Run the task sequentially in the main process
    tstart = time.time()
    for run in range(nruns):
        naive_largest_prime()
    tend = time.time()
    print("Native: %f"%(tend - tstart))


    # Run as `nruns` paralellel Threads
    tsetup = time.time()
    threads = [threading.Thread(target=naive_largest_prime) for i in range(nruns)]
    tstart = time.time()
    for thread in threads:
        thread.start()
    tprocess = time.time()
    for thread in threads:
        thread.join()
    tend = time.time()
    print("Threading: %f"%(tend - tstart))
    print("Threading raw: %f"%(tend - tprocess))


    # Run as `nruns` parallel Processes
    tsetup = time.time()
    processes = [multiprocessing.Process(target=naive_largest_prime) for i in range(nruns)]
    tstart = time.time()
    for process in processes:
        process.start()
    tprocess = time.time()
    for process in processes:
        process.join()
    tend = time.time()
    print("Processing: %f"%(tend - tstart))
    print("Processing raw: %f"%(tend - tprocess))


