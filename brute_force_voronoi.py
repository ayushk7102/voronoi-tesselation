import cv2 as cv
import numpy as np
import randomcolor 

N = 500
N_points = 30
grid = np.zeros((N, N, 3),  np.uint8) + 255

rand_color = randomcolor.RandomColor()
str_colors = rand_color.generate( count=N_points, format_='rgb')
colors = []

for color in str_colors:
	col = tuple(map(int, color[4:-1].split(', ')))
	colors.append(col)


points = [(int(np.random.rand() * N), int(np.random.rand() * N)) for i in range(N_points)]

print('Points: ', points)
i = 0 
for point, color in zip(points, colors):
	cv.circle(grid, point, 4, color, -1)
	
	i+=1


def euclid_dist(p1, p2):
	return ((p2[1] - p1[1])**2 + (p2[0] - p1[0])**2)**0.5

for i in range(N):
	for j in range(N):
		p1 = (i, j)
		color = (0, 0, 0)
		min_dist = euclid_dist(p1 , points[0])
		min_idx = 0
		for k in range(N_points):
			d = euclid_dist(p1 , points[k])
			if(d < min_dist):
				min_idx = k
				min_dist = d
		print('Min dist: ', d, 'Min idx: ', min_idx)
		# cv.circle(grid, points[min_idx], 5, (0, 0, 255), 2)
		grid[j, i] = colors[min_idx]



i = 0 
for point, color in zip(points, colors):
	cv.circle(grid, point, 4, (0, 0, 0), -1)
	i+=1


cv.imshow('grid', grid)
cv.waitKey(0)