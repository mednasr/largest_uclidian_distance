from scipy.spatial import distance
import numpy as np

coords = [(2810125  , 1002710),(4023834  , 4748684),(1312573 , 8418602), (4038083 , 9103890),(8637793  , 2528606),(988534 , 8667395),(8899296 , 9013490)]


dists = distance.cdist(coords, coords, 'euclidean')
print("\nplace",np.argmax(dists),"Is the most isolated Place\n \nThe Distance between this place and other places is :",np.max(dists))
