import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
from scripts.voronoi import voronoi_finite_polygons_2d
from scripts.math import generate_points, convert_ind_to_coords, get_points_inside_polygon, calc_center_of_mass, interpolate_matrices
from scripts.displaying import display_regions
import matplotlib.pyplot as plt

# #-----------------------------------
# points = np.array([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2],
#                 [2, 0], [2, 1], [2, 2]])
# vor = Voronoi(points)
# regions, vertices = voronoi_finite_polygons_2d(vor,1000)

# # Wyswietl regiony
# fig, ax = plt.subplots()
# voronoi_plot_2d(vor, ax)
# for region in regions:
#     polygon = vertices[region]
#     ax.fill(*zip(*polygon), alpha=0.4)
# ax.set_xlim([points[:,0].min()-1, points[:,0].max()+1])
# ax.set_ylim([points[:,1].min()-1, points[:,1].max()+1])
# plt.show()
#
# #-----------------------------------
# num_points = 100
# width = 300
# height = 300

# points = generate_points(num_points, width, height)

# vor = Voronoi(points)
# regions, vertices = voronoi_finite_polygons_2d(vor, max(width, height))

# display_regions(vor, regions, vertices, points)

# #-----------------------------------

# num_points = 100
# width = 300
# height = 300

# points = generate_points(num_points, width, height)

# vor = Voronoi(points)
# regions, vertices = voronoi_finite_polygons_2d(vor, max(width, height))

# points_inside_polygon = []
# for region in regions:
#     polygon = vertices[region]

#     points_inside_polygon = get_points_inside_polygon(polygon, width, height)
#     points_inside_polygon = np.array(points_inside_polygon)
    
#     image = np.zeros((height, width), dtype=np.uint8)
#     image[points_inside_polygon[:, 1], points_inside_polygon[:, 0]] = 255

#     mask_center = np.mean(points_inside_polygon, axis=0)
    
#     plt.imshow(image, cmap='gray')
#     plt.plot(mask_center[0], mask_center[1], 'ro')
#     plt.show()
#-----------------------------------

# def create_gradient(width=300, height=300):
#     """
#     Create a gradient image of specified width and height.
#     """
#     gradient = np.linspace(0, 1, height)  # generate values from 0 to 1
#     gradient = np.repeat(gradient[:, np.newaxis], width, axis=1)  # repeat gradient for each column
#     return gradient

# num_points = 10
# width = 300
# height = 300

# img_gray = create_gradient(width, height)
# #img_gray = np.zeros((height, width))

# points = generate_points(num_points, width, height)

# vor = Voronoi(points)
# regions, vertices = voronoi_finite_polygons_2d(vor, max(width, height))

# points_inside_polygon = []
# for point, region in zip(points, regions):
#     polygon = vertices[region]

#     points_inside_polygon = get_points_inside_polygon(polygon, width, height)
    
#     image = np.zeros((height, width), dtype=np.uint8)
#     image[points_inside_polygon[:, 1], points_inside_polygon[:, 0]] = 255

#     mask_center_avr = np.mean(points_inside_polygon, axis=0)
    
#     mass = img_gray[points_inside_polygon[:, 1], points_inside_polygon[:, 0]]
#     mass = (mass - mass.min()) / (mass.max() - mass.min()) ** 4 # normalize mass and increase contrast
#     mask_center_mass = calc_center_of_mass(points_inside_polygon, mass)
    

#     # Tutaj umieść kod do aktualizacji obrazu
#     plt.imshow(image, cmap='gray')
#     plt.plot(mask_center_mass[0], mask_center_mass[1], 'ro')
#     plt.plot(mask_center_avr[0], mask_center_avr[1], 'bo')
#     plt.plot(point[0], point[1], 'go')
#     plt.pause(0.01)
#     plt.waitforbuttonpress()
#     plt.clf()
#-----------------------------------
from PIL import Image
import io
import imageio

def calc_centroids_of_regions(regions, vertices, img_gray):
    centroids = []
    for region in regions:
        polygon = vertices[region]
        points_inside_polygon = get_points_inside_polygon(polygon, img_gray.shape[1], img_gray.shape[0])
        mass = img_gray[points_inside_polygon[:, 1], points_inside_polygon[:, 0]] + 1
        mask_center_mass = calc_center_of_mass(points_inside_polygon, mass)
        centroids.append(mask_center_mass)
        
    return centroids

num_points = 30
width = 300
height = 300
iterations = 40

img_gray = np.zeros((height, width))

points = generate_points(num_points, width, height)

frames = []
for ii in range(iterations):
    
    vor = Voronoi(points)
    regions, vertices = voronoi_finite_polygons_2d(vor, max(width, height))
    centroids = calc_centroids_of_regions(regions, vertices, img_gray)
    
    points = interpolate_matrices(points, centroids, 0.7) # move points towards centroids
    
    # Tutaj umieść kod do aktualizacji obrazu
    #plt.imshow(img_gray, cmap='gray')
    plt.plot(points[:, 0], points[:, 1], 'ro')
    
    for region in regions:
        polygon = vertices[region]
        polygon_stacked = np.vstack((polygon, polygon[0]))
        plt.plot(polygon_stacked[:, 0], polygon_stacked[:, 1], 'b-')
    
    plt.xlim(0, width)
    plt.ylim(0, height)
    
    plt.pause(0.01)
    #plt.waitforbuttonpress()
    
    # Zapisywanie obrazu do zmiennej
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    frame = Image.open(buf)
    frames.append(np.array(frame))
    plt.clf()
    
imageio.mimsave('voronoi.gif', frames, duration=0.1, loop=0)

