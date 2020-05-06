import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import markdown
import math
print
print("Hello Github!")
print("Hello Capstone Project Course!")
html = markdown.markdown("<b>A ver qué onda</b>")
print(html)
x = np.linspace(0, 10, 100)

# Plot the data
plt.plot(x, x**2, label='linear')

# Add a legend
plt.legend()

# Show the plot
plt.show()

print(0.3)
print(math.fsum([0.1,0.1,0.1]))
print(0.1+0.1+0.1)