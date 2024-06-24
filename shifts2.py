import numpy as np
from scipy.signal import correlate

def find_shifts(f, g, x_vals):
    f_vals = np.array([f(x) for x in x_vals])
    g_vals = np.array([g(x) for x in x_vals])

    # Calculate vertical shift
    # differences = g_vals - f_vals
    # b = np.mean(differences)
    b = np.max(g_vals) - np.max(f_vals)

    # Adjust g for vertical shift
    # g_adj = g_vals - b

    # Calculate cross-correlation to find horizontal shift
    # correlation = correlate(f_vals, g_adj, mode='full')
    # lag = np.argmax(correlation) - (len(f_vals) - 1)
    lag = x_vals[np.argmax(f_vals)] - x_vals[np.argmax(g_vals)]

    return lag, b

# Example functions
f = lambda x: -2*x*x + 8            # np.sin(x)
g = lambda x: -2*(x-3)*(x-3) + 5    # np.sin(x - 2) + 3

# Sample points
x_vals = np.linspace(-10, 10, 1000)

# Find shifts
a, b = find_shifts(f, g, x_vals)
print(f"Horizontal shift: {a}")
print(f"Vertical shift: {b}")
print(f"g(x) = f(x + {a:0.4f}) + {b:0.4f}")
