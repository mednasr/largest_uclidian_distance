import math, itertools

data = """1312573 8418602 4038083 9103890 8899296 9013490 988534 8667395 2810125 1002710 4023834 4748684 8637793 2528606"""

def calc_distance(c1, c2):
    return math.hypot(c2[0] - c1[0], c2[1] - c1[1])

results = []

for row in data.split("\n"):
    cols = [float(col) for col in row.split(" ") if len(col)]
    max_distance = 0
    for c1,c2 in itertools.permutations(zip(cols[1:], cols[2:]), 2):
        max_distance = max(max_distance, calc_distance(c1,c2))

    results.append((max_distance, cols[0]))

results.sort()

for distance, frame in results:
    print ("%-15s %f" % (frame, distance))