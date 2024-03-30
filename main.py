from PIL import Image
import numpy as np
from scripts.math import generate_points_from_img, interpolate_matrices
import matplotlib.pyplot as plt
from scripts.voronoi import voronoi_finite_polygons_2d, calc_centroids_of_regions
from scipy.spatial import Voronoi

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
    
    
