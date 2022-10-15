# Histogram
# compare

import matplotlib.pyplot as plt

life_exp= [43.8, 76.4, 72.31, 42.73, 75.32, 81.23, 79.829, 75.35, 64.62, 79.1]
life_exp1950= [28.8, 55.23, 43.08, 30.02, 62.48, 69.12, 66.8, 50.94, 37.48, 68.0]

# Histogram of life_exp, 15 bins
plt.hist(life_exp, bins=15)

# Show and clear plot
plt.show()
plt.clf()

# Histogram of life_exp1950, 15 bins
plt.hist(life_exp1950, bins=15)

# Show and clear plot again
plt.show()
plt.clf()