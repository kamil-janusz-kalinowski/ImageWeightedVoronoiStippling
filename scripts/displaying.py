import matplotlib.pyplot as plt
from scipy.spatial import voronoi_plot_2d

def display_regions(vor, regions, vertices, points):
    # Wyswietl regiony
    fig, ax = plt.subplots()
    voronoi_plot_2d(vor, ax)
    for region in regions:
        polygon = vertices[region]
        ax.fill(*zip(*polygon), alpha=0.4)
    ax.set_xlim([points[:,0].min()-1, points[:,0].max()+1])
    ax.set_ylim([points[:,1].min()-1, points[:,1].max()+1])
    plt.show()