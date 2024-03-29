import numpy as np
import matplotlib.path as mplpath

def calculate_centroid_from_mask_and_img(mask, image_gray):
    indices = np.where(mask)
    x = np.average(indices[1], weights=(image_gray[indices] + 1))
    y = np.average(indices[0], weights=(image_gray[indices] + 1))
    centroid = [x, y]
    return centroid

def interpolate_matrices(matrix1, matrix2, factor):
    return np.add(matrix1, np.multiply(factor, np.subtract(matrix2, matrix1)))


def generate_points(num_points, width, height):
    return np.random.rand(num_points, 2) * np.array([width, height])


def convert_ind_to_coords(inds, width): 
    return np.array([inds % width, inds // width]).T


def get_points_inside_polygon(polygon, width, height):
    x, y = np.meshgrid(np.arange(width), np.arange(height))
    path = mplpath.Path(polygon)
    mask = path.contains_points(np.vstack((x.flatten(), y.flatten())).T)
    inds_inside_polygon = np.where(mask)[0]
    
    points_inside_polygon = convert_ind_to_coords(inds_inside_polygon, width)
    
    return points_inside_polygon

def calc_center_of_mass(pos, mass):
    return np.average(pos, weights=mass, axis=0)