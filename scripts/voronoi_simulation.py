import numpy as np
from scipy.spatial import Voronoi
import matplotlib.pyplot as plt
from scripts.math_custom import generate_points_from_img, interpolate_matrices
from scripts.voronoi import voronoi_finite_polygons_2d, calc_centroids_of_regions
from scripts.animation import get_current_plot_as_img, save_frames_as_gif

from PIL import Image
import imageio

class VoronoiSimulation:
    def __init__(self, img_gray: np.ndarray, num_points= 100, move_factor=0.5):
        self.num_points = num_points
        self.width = img_gray.shape[1]
        self.img_gray = img_gray
        self.height = img_gray.shape[0]
        self.points = self.generate_new_points()
        self.voronoi = Voronoi(self.points)
        self.move_factor = move_factor
        self.regions = []
        self.vertices = []
        self.radius = max(self.width, self.height)/2
        
    def generate_new_points(self):
        return generate_points_from_img(self.img_gray ,self.num_points)
        
    def update_voronoi(self):
        self.voronoi = Voronoi(self.points)
        regions, vertices = voronoi_finite_polygons_2d(self.voronoi, self.radius)
        self.regions = regions
        self.vertices = vertices
        
    def update_points(self):
        centroids = calc_centroids_of_regions(self.regions, self.vertices, self.img_gray)
        self.points = interpolate_matrices(self.points, centroids, self.move_factor)
        
    def plot_voronoi(self):
        plt.clf()
        # Show image, points, and region edges
        plt.imshow(self.img_gray, cmap='gray')
        plt.plot(self.points[:, 0], self.points[:, 1], 'b.')
        for region in self.regions:
            region = np.append(region, region[0])
            plt.plot(self.vertices[region, 0], self.vertices[region, 1], 'r-')
        plt.xlim(0, self.img_gray.shape[1])
        plt.ylim(self.img_gray.shape[0], 0)
        plt.pause(0.005)
    
    def run_simulation(self, iterations, save_gif=False, gif_name=None):
        self.generate_new_points()
        
        if save_gif and gif_name is not None:
            frames = []
        
        for ii in range(iterations):
            self.update_voronoi()
            self.update_points()
            
            self.plot_voronoi()
            
            if save_gif and gif_name is not None:
                frames.append(get_current_plot_as_img())
        
        if save_gif and gif_name is not None:
            save_frames_as_gif(frames, gif_name)