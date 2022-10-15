# Customization
# Label and Title

import matplotlib.pyplot as plt

gdp_cap= [974.5803384, 5937.029525999999, 6223.367465, 4797.231267, 12779.37964, 34435.367439999995]
life_exp=[43.828, 76.423, 72.301, 42.731, 75.32, 81.235]

# Basic scatter plot, log scale
plt.scatter(gdp_cap, life_exp)
plt.xscale('log') 

# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)


# Add title
plt.title(title)

# After customizing, display the plot
plt.show()