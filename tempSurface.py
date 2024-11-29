import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata

# Data: Latitude, Longitude, and Temperatures for 7 days
locations = {
    "San Francisco": [37.7749, -122.4194],
    "Pleasanton": [37.6624, -121.8747],
    "Livermore": [37.6819, -121.7680],
    "Dublin": [37.7022, -121.9358],
    "San Ramon": [37.7799, -121.9780],
    "Fremont": [37.5483, -121.9886],
    "Tracy": [37.7397, -121.4252],
    "San Jose": [37.3382, -121.8863],
    "Walnut Creek": [37.9101, -122.0652],
    "Palo Alto": [37.4419, -122.1430]
}

# Convert to DataFrame
data = {
    "Latitude": [locations[city][0] for city in locations],
    "Longitude": [locations[city][1] for city in locations],
    "Day 1": [55, 57, 57, 57, 55, 58, 57, 58, 55, 57],
    "Day 2": [55, 57, 55, 57, 57, 57, 55, 58, 57, 58],
    "Day 3": [54, 56, 56, 57, 56, 59, 56, 58, 54, 57]
}

df = pd.DataFrame(data)

# Prepare grid for interpolation
grid_lat, grid_lon = np.mgrid[
    df["Latitude"].min():df["Latitude"].max():100j,
    df["Longitude"].min():df["Longitude"].max():100j
]

# Choose a day to visualize (e.g., Day 1)
day_to_plot = "Day 1"

# Interpolation
temperature_grid = griddata(
    (df["Latitude"], df["Longitude"]), 
    df[day_to_plot], 
    (grid_lat, grid_lon), 
    method='cubic'
)

# Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(
    grid_lon, grid_lat, temperature_grid, cmap="coolwarm", edgecolor='none'
)

ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.set_zlabel("Temperature (°F)")
ax.set_title(f"3D Temperature Surface - {day_to_plot}")
fig.colorbar(surf, shrink=0.5, aspect=10, label="Temperature (°F)")

plt.show()
