import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-<style>')

fig = plt.figure()
ax = fig.add_subplot(111)

A = [x*x for x in range(10)]
B = [x*x*x for x in range(10)]
plt.plot(A)
plt.plot(B)

plt.show()


