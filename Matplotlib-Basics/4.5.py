# Customization
# Additional Customizations (Adding Text)

import matplotlib.pyplot as plt
import numpy as np

gdp_cap= [974.5803384, 5937.029525999999, 6223.367465, 4797.231267, 12779.37964, 34435.367439999995]
life_exp=[43.828, 76.423, 72.301, 42.731, 75.32, 81.235]
pop=[121.17, 1113.44, 222.89, 227.19,441.1,120.1]
col=['red', 'green', 'blue', 'blue', 'pink', 'black']

# Scatter plot
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Additional customizations
plt.text(11000, 75, 'India')
plt.text(5700, 77, 'China')

# Add grid() call
plt.grid(True)

# Show the plot
plt.show()