# Histogram
# Python sets the number of bins to 10 in that case.

import matplotlib.pyplot as plt

life_exp=[43.8, 76.4, 72.31, 42.73, 75.32, 81.23, 79.829, 75.35, 64.62, 79.1]

# Create histogram of life_exp data

plt.hist(life_exp)
# Display histogram
plt.show()