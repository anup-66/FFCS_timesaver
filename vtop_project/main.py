# import numpy as np
# import matplotlib.pyplot as plt
#
# # create a 2D numpy array to represent the grid
# grid = np.zeros((12, 11))
#
# # fill some cells with data
# grid[1, 2] = 1
# grid[3, 5] = 1
# grid[5, 8] = 1
#
# # set the cell width and height
# cell_width = 0.5
# cell_height = 0.5
#
# # create a figure and axis object
# fig, ax = plt.subplots()
#
# # plot the grid as a heatmap with adjusted cell size and extent
# ax.imshow(grid, cmap='Greens')#, extent=[0, grid.shape[1]*cell_width, grid.shape[0]*cell_height, 0])
#
# # set the x and y tick labels
# ax.set_xticks(np.arange(-0.5, 10, 1))
# ax.set_yticks(np.arange(-0.5, 11, 1))
# ax.set_xticklabels([])
# ax.set_yticklabels([])
#
# # add grid lines
# ax.grid(which='major', color='black', linestyle='-', linewidth=1)
#
# # add text to each cell
# # for i in range(grid.shape[0]):
# #     for j in range(grid.shape[1]):
# #         text = ax.text(j*cell_width+cell_width/2, i*cell_height+cell_height/2, str(grid[i, j]), ha='center', va='center', color='w')
# for i in range(grid.shape[0]):
#     text = ax.text(0,i,"A1 + Ta1",ha = "center",va = "center",color = "r",fontsize=min(cell_width, cell_height)*10)
# # show the plot
# plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Create a 2D numpy array to represent the grid
grid = np.zeros((10, 10))

# Fill some cells with data
grid[1, 2] = 1
grid[3, 5] = 1
grid[5, 8] = 1

# Set the cell width and height
cell_width = .5
cell_height = 2

# Create a figure and axis object
fig, ax = plt.subplots()

# Add text to each cell and color the cells
# for i in range(grid.shape[0]):
#     for j in range(grid.shape[1]):
#         ax.add_patch(plt.Rectangle((j*cell_width, i*cell_height), cell_width, cell_height, fill=True, facecolor='green', edgecolor='black'))
#         ax.text(j*cell_width+cell_width/2, i*cell_height+cell_height/2, str(grid[i,j]), ha='center', va='center', color='white')
ax.add_patch(plt.Rectangle((j*cell_width, i*cell_height), cell_width, cell_height, fill=True, facecolor='green', edgecolor='black'))
ax.text(j*cell_width+cell_width/2, i*cell_height+cell_height/2, str(grid[i,j]), ha='center', va='center', color='white')

# Set the x and y tick labels
ax.set_xticks(np.arange(0, 10*cell_width, cell_width))
ax.set_yticks(np.arange(0, 10*cell_height, cell_height))
ax.set_xticklabels([])
ax.set_yticklabels([])

# Add grid lines
ax.grid(which='major', color='black', linestyle='-', linewidth=1)

# Set the plot axis limits
ax.set_xlim([0, 10*cell_width])
ax.set_ylim([0, 10*cell_height])

# Show the plot
plt.show()
