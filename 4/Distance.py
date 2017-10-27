import numpy as np
import scipy.spatial.distance as distance

points = np.array([(5 , 4),(4 , 3),(3 , 2),(2 , 1)])

dist = distance.pdist(points)
print (dist.max())
print (dist.min())
print ( "The most isolated point is : ",np.argmax(dist))

