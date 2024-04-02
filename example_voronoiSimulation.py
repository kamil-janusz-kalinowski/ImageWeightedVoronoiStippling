
import numpy as np
from PIL import Image
from scripts.voronoi_simulation import VoronoiSimulation


img_gray = np.array(Image.open('materials\cup_1.png').convert('L'))
threshold = 40
img_gray[img_gray < threshold] = 0

voronoi_sim = VoronoiSimulation(img_gray)
voronoi_sim.run_simulation(30, save_gif=True, gif_name='voronoi_simulation.gif')