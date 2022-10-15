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

plt.yticks([0,2,4,6,8],['0B','2B','4B','6B','8B'])

# show
plt.show()
plt.clf()