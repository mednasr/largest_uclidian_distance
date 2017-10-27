import math
import numpy as np

points = [(472765.09, 6191522.78, 13.0), (472764.82, 6191524.09, 9.0),
          (472763.8, 6191525.68, 8.0), (472764.07, 6191524.39, 16.0)]
points += [points[0]]
dist3D = lambda a, b: math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)
dists = sorted(dist3D(points[i], points[i+1]) for i in range(len(points)-1))
min_dist, max_dist = dists[0], dists[-1]

mean_dist = np.average(dists)

print ('min_dist: {:.2f}, mean_dist: {:.2f}, max_dist: {:.2f}'.format(
    min_dist, mean_dist, max_dist))