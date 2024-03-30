# Voronoi Diagram Animation Generator
This repository contains Python scripts for generating dynamic Voronoi diagrams. Voronoi diagrams are a partitioning of a plane into regions based on distance to points in a specific subset of the plane. The scripts in this repository use this concept to create interesting animations.

There are two main scripts in this repository:

## main.py: 
This script generates a dynamic Voronoi diagram from a set of points. It starts by generating an initial set of points and an empty image. Then, it iteratively calculates the Voronoi diagram for the current points, moves the points towards the centroids of the Voronoi regions, and updates the image. The updated Voronoi diagram is visualized in each iteration. Finally, it saves the sequence of updated images as a gif.

## image_based.py: 
This script uses an image to generate a dynamic Voronoi diagram. It starts by opening an image and converting it to grayscale. Then, it generates an initial set of points based on the grayscale image. In each iteration, it calculates the Voronoi diagram for the current points, identifies the finite polygons of the Voronoi diagram, calculates the centroids of these regions, and moves the points towards the centroids. The updated Voronoi diagram is visualized in each iteration by overlaying the points on the grayscale image. The visualization is cleared at the end of each iteration to prepare for the next one.

The repository also includes several helper scripts in the scripts directory for tasks such as animation, math operations, and Voronoi calculations.

### Requirements:
- PIL (Pillow)
- NumPy
- Matplotlib
- SciPy
