# largest Euclidian distance
### At WRLD we are bringing maps to life - it's important for us to be able to analyze data about the map features.

### Consider a map that has the following properties;
	- the map is two dimensional
	- the map is perfectly square with dimensions 10000000x10000000
	- the map has an associated set of many features
	- the map does not "wrap around"
### Each feature on the map is described by a 2D coordinate in the range (0, 0) to (10000000, 10000000).

We would like to find the most isolated feature on the map, where the "most isolated feature" is the feature that is
furthest (largest Euclidian distance) from any other feature. Because the map does not "wrap around", this should be a
direct distance across the map.

<----10000000---->
 ---------------      -
| A             |     |
|               |     |
|               |  10000000
|               |     |
|          B  C |     |
|        E   D  |     |
 ---------------      -

In the example above, A is the most isolated feature on the square map with edge length 10000000.

We would like you to write a program that reads in many features from standard input, and outputs the name of the most isolated
feature to standard output. The format of the input is the feature name, x coordinate and y coordinate separated by spaces.
Each feature is on a new line. There may be any number of features between 1 and 100000. The program should
be fast, so the algorithm must be better than n^2.


