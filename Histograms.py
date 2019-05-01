import matplotlib.pyplot as plt
import numpy as np

# Generate a list of 1000 random values between 0.0 and 1.0
x = np.random.normal(size = 1000)

# Plot a histogram of this data, dividing it up into 30 bins
plt.hist(x, normed=True, bins=30)

# Add a label and show the histogram
plt.ylabel('Probability');
plt.show()
