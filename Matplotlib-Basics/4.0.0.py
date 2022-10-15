# Customization

import matplotlib.pyplot as plt

year=[2049, 2059, 2069, 2079]
pop=[2.17, 3.44, 6.89, 7.19]


# plot
plt.plot(year,pop)

# customizing
plt.xlabel("Year")
plt.ylabel("Population")
plt.title("Nepal's Population")

# show
plt.show()