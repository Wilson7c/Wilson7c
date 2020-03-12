import matplotlib.pyplot as plt
import random

plt.figure(1)

plt.plot([120, 40, 10, 0])
plt.plot([1, 2, 3, 4, 5, 6], [1, 4, 9, 16, 25, 36])

plt.figure(2)

x1 = [x for x in range(1, 101)]
y1 = [y ** 2 for y in x1]

plt.plot(x1, y1, color='green', marker='*', markersize=10, linestyle='--', alpha=0.5, label="myPlot")

plt.xlabel('time (seconds)')
plt.ylabel('excitement level (YAYS)')
plt.title('Example Plot')
plt.axis([0, 11, 0, 120])



plt.show()

