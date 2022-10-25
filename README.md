# Algorithms for Voronoi Tessellation
A Voronoi tessellation is a partition of a plane into regions, or cells, close to each of a given set of points. This mathematical principle has many applications in flight navigation, epidemiology, and even guiding the movement of AI agents. 

This repo contains a few of my own implementations of algorithms to partition a plane into convex Voronoi cells.

Visualised using randomcolor and OpenCV.

## Brute force method

The simplest, inefficient approach, which produces deterministic output in *O(n^3)* time:

![grid_screenshot_12 05 2022](https://user-images.githubusercontent.com/65803868/168063363-03d1e66e-cff7-46b1-a782-241ef49d69f4.png)


## Jump flooding algorithm

This is a parallelizable variant of graph-flooding that improves the complexity of constructing Voronoi diagrams to *O* $(n^2 log n)$ . 

To compute the Voronoi diagram for a 2D grid of size $n×n$ with a given set of seeds at some grid points, we are interested to propagate position information of each seed *s* to each of its neighbouring points, assigning colors to the neighbours according to a distance-based heuristic. 

Each neighbouring point is selected at a step size of $k$ $&epsilon;$  { ${n/2, n/4, n/8....}$  } for each iteration of JFA.



![jfa](https://user-images.githubusercontent.com/65803868/197709822-3d0db7ae-84f5-4e58-9bff-6d22354cdd2c.gif)
