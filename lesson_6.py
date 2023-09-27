import time

import adi
import matplotlib.pyplot as plt
import numpy as np


# Create radio
sdr = adi.Pluto("ip:192.168.2.1")

# Configure properties
sdr.rx_lo = 2437000000

# Collect data
for r in range(100):
    rx = sdr.rx()
    plt.clf()
    plt.plot(rx.real)
    plt.plot(rx.imag)
    plt.draw()
    plt.pause(0.05)
    time.sleep(0.1)

plt.show()
