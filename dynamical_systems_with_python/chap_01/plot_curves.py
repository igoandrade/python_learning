"""
Name:           plot_curves.py
Description:    A program that plots two curves on on graph.
"""

import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2.0, 0.01)
c = 1 + np.cos(2 * np.pi * t)
s = 1 + np.sin(2 * np.pi * t)

plt.plot(t, s, 'r--', t, c, 'b--')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (mV)')
plt.title('Voltage-time plot')
plt.grid(True)
plt.savefig("voltage_time_plot.png")
plt.show()