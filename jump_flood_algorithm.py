import cv2 as cv
import numpy as np
import randomcolor 

N = 500
N_points = 30
# metric = 'euclidean' 
metric = 'manhattan'

grid = np.zeros((N, N, 3),  np.uint8) + 255

rand_color = randomcolor.RandomColor()
str_colors = rand_color.generate( count=N_points, format_='rgb')
colors = []

for color in str_colors:
	col = tuple(map(int, color[4:-1].split(', ')))
	colors.append(col)


points = [(int(np.random.rand() * N), int(np.random.rand() * N)) for i in range(N_points)]
pcopy = points
print('Points: ', points)
i = 0 
grid_copy = grid.copy()
for point, color in zip(points, colors):
	cv.circle(grid_copy, point, 4, color, -1)
	grid[point[1], point[0]] = color
	i+=1


def dist(p1, p2):
	if(metric == 'euclidean'):
		return ((p2[1] - p1[1])**2 + (p2[0] - p1[0])**2)**0.5

	if(metric == 'manhattan'):
		return abs(p2[1] - p1[1]) + abs(p2[0] - p1[0])	

# cv.imshow('grid', grid)
# cv.waitKey(0)


seeds = points

point_dict = color_dict =dict()

for point, color in zip(points, colors):
	point_dict[str(np.array(color))] = point
	color_dict[point] = color

k = N/2

i = j = [-1, 0, 1]

it = 0
ct = 0

while k>0:

	print('iter#',it, '\tk=',k)
	it+=1
	for p in seeds:

		px, py = p
		color = grid[p[1], p[0]]

		for dx in i:
			for dy in j:
				if dx == 0 and dy == 0:
					continue

				new_p = x, y = int(px + k*dx), int(py + k*dy)
				# print(new_p)


				#if the new seed falls out of bounds of the graph
				if x < 0 or y < 0 or x >= N or y >= N:
					continue


				if (grid[y, x] == color).all(): #already assigned to current seed
					continue


				if (grid[y, x] == 255).all(): #not assigned to a seed yet
					grid[y, x] = color
					# cv.imwrite('/home/ayush/Desktop/Stuff/Random/voronoi/voronoi-tessellation/jfa/'+str(ct)+'.jpg', grid)
					# ct +=1

					seeds.append(new_p)


				else:
					p1 = point_dict[str(grid[y, x])] #find seed which current point is mapped to
					p2 = point_dict[str(color)] 

					d1 = dist(p1, new_p)
					d2 = dist(p2, new_p)

					if d2 < d1:
						grid[y, x] = color
						

						# cv.imshow('grid', grid)
						# cv.waitKey(1)




	k = k//2

	cv.imshow('grid', grid)
	cv.waitKey(1)
	cv.imwrite('/home/ayush/Desktop/Stuff/Random/voronoi/voronoi-tessellation/jfa/'+str(ct)+'.jpg', grid)
	ct +=1


exit()

for p in seeds:

	px, py = p

	for dx in i:
		for dy in j:
			if dx == 0 and dy == 0:
				continue
			
			new_p = x, y = int(px + k*dx), int(py + k*dy)

			if x < 0 or y < 0 or x >= N or y >= N:
				continue

			it+=1

			grid[y, x] = color

			color_dict[new_p] = color

			seeds.append(new_p)
			print('iter', it)

			cv.imshow('grid', grid)
			cv.waitKey(1)


cv.imshow('grid', grid)
cv.waitKey(0)



# for p in pcopy:
# 	cv.circle(grid, p, 4, (0, 0, 0), -1)
# 	cv.imwrite('/home/ayush/Desktop/Stuff/Random/voronoi/voronoi-tessellation/jfa/'+str(ct)+'.jpg', grid)
