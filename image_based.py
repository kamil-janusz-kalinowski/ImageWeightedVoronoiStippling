import numpy as np
from scripts.math import generate_points_from_img, interpolate_matrices
import matplotlib.pyplot as plt
from scripts.voronoi import voronoi_finite_polygons_2d, calc_centroids_of_regions
from scipy.spatial import Voronoi
from PIL import Image

# This script uses an image to generate a dynamic Voronoi diagram. 
# It starts by opening an image and converting it to grayscale. 
# Then, it generates an initial set of points based on the grayscale image. 
# In each iteration, it calculates the Voronoi diagram for the current points, 
# identifies the finite polygons of the Voronoi diagram, calculates the centroids of these regions, 
# and moves the points towards the centroids. 
# The updated Voronoi diagram is visualized in each iteration by overlaying the points on the grayscale image. 
# The visualization is cleared at the end of each iteration to prepare for the next one.

num_points = 200
img_gray = np.array(Image.open('materials\cup_1.png').convert('L'))

points = generate_points_from_img(img_gray, num_points)

# # Show image and points
# plt.imshow(img_gray, cmap='gray')
# plt.plot(points[:, 0], points[:, 1], 'b.')
# plt.show()

iter_num = 100
for ii in range(iter_num):
    vor = Voronoi(points)
    regions, vertices = voronoi_finite_polygons_2d(vor, max(img_gray.shape))
    centroids = calc_centroids_of_regions(regions, vertices, img_gray)
    
    points = interpolate_matrices(points, centroids, 0.5) # move points towards centroids
    
    # Show image and points
    plt.imshow(img_gray, cmap='gray')
    plt.plot(points[:, 0], points[:, 1], 'b.')
    #plt.pause(0.01)
    plt.clf()