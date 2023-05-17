import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('data.txt')
settings = np.loadtxt('settings.txt')
volts = data * settings[1]

time = np.arange(len(data)) * settings[0]

# Create figure and axes 
fig, ax = plt.subplots()

# Plot voltage(time)
ax.plot(time, volts, color='green', linestyle='-', marker='o', markersize=1, markerfacecolor='red', label='V(t)')

# Set maximum and minimum values for the scale
ax.set_xlim(np.min(time), 10)
ax.set_ylim(np.min(volts), 3)

# Set x and y axis labels
ax.set_xlabel('Time, s')
ax.set_ylabel('Voltage, V')

# Set the title of the graph
ax.set_title('RC condenser charging and discharging process')

# Configure grid
ax.grid(True, linestyle=':', linewidth=0.4, color='gray')
ax.minorticks_on()
ax.grid(True, which='minor', linestyle=':', linewidth=0.2, color='lightgray')

# Add legend
ax.legend()

# Text for charging and discharging time
plt.text(1.78, 1.5, r'$Charging \; time \approx 60.6 \;s  $', fontsize=10, color='blue')
plt.text(1.78, 1.3, r'$Charging \; time \approx 75.5 \;s  $', fontsize=10, color='blue')


# Save the graph to a file in .svg format
plt.savefig('graph.svg', format='svg')

# Show the plot
plt.show()
