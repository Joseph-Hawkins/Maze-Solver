import numpy as np
## in order to use matplotlib library, you need to include the library (import)
import matplotlib.pyplot as plt

## create a maze data structure
## the Z below is a 2D binary matrix with dimension is 101*101
## each Z has 60% chance to be 0 and 40% chance to be 1
Z = np.random.choice([0, 1], size=[101, 101], p=[.60, .40])

## This is where you start to plot the maze
plt.figure()
# The parameters in the main plotting function
# (1) Z: the input maze you want to visualize
# (2) cmap: This indicates the color map you're using. Here it is a binary map(white & black)
# (3) interpolation: by setting to 'nearest', the image becomes more clear. You can delete it to 
#     see the difference.
plt.imshow(Z, cmap=plt.cm.binary, interpolation='nearest')

# This line hides the x and y coordinate. You can delete it to see the difference
plt.xticks([]), plt.yticks([])

# This last line is a must to trigger the visualization
plt.show()
