# Customization
# Tick

import matplotlib.pyplot as plt

gdp_cap= [974.5803384, 5937.029525999999, 6223.367465, 4797.231267, 12779.37964, 34435.367439999995]
life_exp=[43.828, 76.423, 72.301, 42.731, 75.32, 81.235]

# Scatter plot
plt.scatter(gdp_cap, life_exp)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')

# Definition of tick_val and tick_lab
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']

# Adapt the ticks on the x-axis
plt.xticks(tick_val,tick_lab)

# After customizing, display the plot
plt.show()