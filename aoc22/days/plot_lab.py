import matplotlib.pyplot as plt
import time
import numpy as np

# Example data
data = [{'x': 1, 'y': 2}, {'x': 3, 'y': 4}, {'x': 5, 'y': 6}]

# Extract x and y values from data
x = [d['x'] for d in data]
y = [d['y'] for d in data]

# Create a figure and axis
fig, ax = plt.subplots()
scatter = ax.scatter(x, y)
# plot = ax.plot(x, y)

# Define the update function
def update(data):
    # global data
    x = [d['x'] for d in data]
    y = [d['y'] for d in data]
    scatter.set_offsets(np.c_[x, y])
    # fig.set_offsets(np.c_[x, y])
    # ax.relim()
    # ax.autoscale_view()
    xmin=min(x); xmax=max(x)
    ymin=min(y); ymax=max(y)
    ax.set_xlim(xmin-0.1*(xmax-xmin),xmax+0.1*(xmax-xmin))
    ax.set_ylim(ymin-0.1*(ymax-ymin),ymax+0.1*(ymax-ymin))

# Start the for loop
for i in range(10):
    data = [{'x': i, 'y': i**2} for i in range(10)]
    update(data)
    plt.pause(1)