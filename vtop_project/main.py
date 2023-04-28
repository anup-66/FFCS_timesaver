
import matplotlib.pyplot as plt
import numpy as np

# Create a 2D numpy array to represent the grid
grid = np.zeros((11, 12))

# Fill some cells with data
grid[1, 2] = 1
# grid[3, 5] = 1
# grid[5, 8] = 1


# Set the cell width and height
cell_width = 2
cell_height = 2

# Create a figure and axis object
fig, ax = plt.subplots()

# Add text to each cell and color the cells
# for i in range(grid.shape[0]):
#     for j in range(grid.shape[1]):
#         ax.add_patch(plt.Rectangle((j*cell_width, i*cell_height), cell_width, cell_height, fill=True, facecolor='green', edgecolor='black'))
#         ax.text(j*cell_width+cell_width/2, i*cell_height+cell_height/2, str(grid[i,j]), ha='center', va='center', color='white')
cell_txt = "a1 + ta1"
# cell_width = len(cell_txt)*0.3
ax.add_patch(plt.Rectangle((0*cell_width, 1*cell_height), cell_width, cell_height, fill=True, facecolor='green', edgecolor='black'))
ax.text(0*cell_width+cell_width/2, 0*cell_height+cell_height/2, cell_txt,ha='center', va='center', color='red')

# Set the x and y tick labels
ax.set_xticks(np.arange(0, 12*cell_width, cell_width))
ax.set_yticks(np.arange(0, 11*cell_height, cell_height))
ax.set_xticklabels([])
ax.set_yticklabels([])

# Add grid lines
ax.grid(which='major', color='black', linestyle='-', linewidth=1)

# Set the plot axis limits
ax.set_xlim([0, 12*cell_width])
ax.set_ylim([0, 11*cell_height])

# Show the plot
plt.show()
from read_xl import read

mod = read()
print(len(mod.returnDict().keys()))
# for i in range():
#     for j in range(len())