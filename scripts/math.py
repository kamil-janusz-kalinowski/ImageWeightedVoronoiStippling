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

def calc_center_of_mass(pos, mass: np.ndarray):
    if np.all(mass == 0):   # if all mass is zero, return the average position
        mass = mass + 1
        
    return np.average(pos, weights=mass, axis=0)

def generate_points_from_img(image_gray, num_points):
    weights = image_gray.flatten()
    indices = np.random.choice(image_gray.size, num_points, replace=False, p=weights/np.sum(weights))
    return convert_ind_to_coords(indices, image_gray.shape[1])

def create_gradient(width=300, height=300):
    """
    Create a gradient image of specified width and height.
    """
    gradient = np.linspace(0, 1, height)  # generate values from 0 to 1
    gradient = np.repeat(gradient[:, np.newaxis], width, axis=1)  # repeat gradient for each column
    return gradient

