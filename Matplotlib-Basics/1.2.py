# Line Plot

import matplotlib.pyplot as plt

gdp_cap= [974.5803384, 5937.029525999999, 6223.367465, 4797.231267, 12779.37964, 34435.367439999995]
life_exp=[43.828, 76.423, 72.301, 42.731, 75.32, 81.235]

# Print the last item of gdp_cap and life_exp
print(gdp_cap[-1])
print(life_exp[-1])


# Make a line plot, gdp_cap on the x-axis, life_exp on the y-axis
plt.plot(gdp_cap,life_exp)

# Display the plot
plt.show()