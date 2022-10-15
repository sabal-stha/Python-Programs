# Histogram
# bins

import matplotlib.pyplot as plt

life_exp=[43.8, 76.4, 72.31, 42.73, 75.32, 81.23, 79.829, 75.35, 64.62, 79.1]

# Build histogram with 5 bins
plt.hist(life_exp,bins=5)

# Show and clean up plot
plt.show()
plt.clf()

# Build histogram with 20 bins
plt.hist(life_exp,bins=20)

# Show and clean up again
plt.show()
plt.clf()