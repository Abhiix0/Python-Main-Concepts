# Analyze a week's temperature data using NumPy
# Demonstrates: Array creation, statistics, filtering, unit conversion, and array inspection

import numpy as np

# Step 1: Create a NumPy array of temperatures (Celsius) for a week
temps_celsius = np.array([30.5, 32.0, 29.5, 31.2, 33.8, 28.9, 34.5])

# Step 2: Basic statistical analysis using NumPy functions
avg_temp = np.mean(temps_celsius)  # Calculate average temperature
max_temp = np.max(temps_celsius)   # Find maximum temperature
min_temp = np.min(temps_celsius)   # Find minimum temperature

print("Weather Stats (°C):")
print(f"Average: {avg_temp:.2f}°C")
print(f"Max: {max_temp}°C | Min: {min_temp}°C")

# Step 3: Filter days with temperature above average
above_avg = temps_celsius[temps_celsius > avg_temp]
print(f"Days above average: {above_avg}")

# Step 4: Convert all temperatures to Fahrenheit using vectorized operations
temps_fahrenheit = (temps_celsius * 9/5) + 32
print(f"Fahrenheit Conversion: {temps_fahrenheit}")

# Step 5: Inspect array structure (shape and dimensions)
print(f"Shape: {temps_celsius.shape}, Dimensions: {temps_celsius.ndim}")
# .shape gives the structure of the array (e.g., (7,) for 1D with 7 elements)
# .ndim gives the number of dimensions (1D, 2D, etc.)

# Additional NumPy Tips (as comments):
# - np.dot()         → Matrix multiplication
# - np.add(), np.subtract(), np.multiply(), np.divide() → Element-wise math operations
# - np.sort()        → Sort arrays
# - np.unique()      → Find unique elements
# - np.linspace(), np.arange() → Create ranges of numbers
# - np.reshape()     → Change the shape of arrays
# - np.isnan(), np.isinf() → Handle NaNs and infinities
# - np.random.*()    → Generate random numbers
# - np.where()       → Conditional selection
# - np.concatenate(), np.vstack(), np.hstack() → Combine arrays
# - np.linalg.*()    → Linear algebra operations (matrix inversion, determinants, etc.)

