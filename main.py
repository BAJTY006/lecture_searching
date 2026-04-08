import time

from matplotlib.testing.jpl_units import Duration

import generators as gen
import matplotlib.pyplot as plt

sizes = [100, 500, 1000, 5000, 10000]
times = []
for size in sizes:
    numbers = gen.ordered_sequence(size)
    target = 78
    start = time.perf_counter()

    for number in numbers:
        if number == target:
            break

    end = time.perf_counter()
    duration = end - start
    print(f"Měření trvalo {duration:.8f} s")
    times.append(duration)





plt.plot(sizes, times)

plt.xlabel("Velikost vstupu")
plt.ylabel("Čas [s]")
plt.title("Ukázkový graf měření")
plt.show()