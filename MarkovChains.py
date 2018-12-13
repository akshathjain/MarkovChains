#Name: Akshath Jain
#Date: 11/25/18
#Purpose: spectral clustering algorithm for 21241 final project

import numpy as np;

#main function
def main():
	x = rank([[1,3,4],[0,2,4],[3,6],[2,4,6],[5,8],[4,6,8],[0,7,9],[0,6,8],[2,9],[0,2,8]]);	
	print(x);

#does the heavy lifting
def rank(ranks):

	#(1) CREATE MATRIX REPRESENTING PAGE LINKS

	#initialize nxn matrix full of zeros
	matrix = [[0 for i in range(0, len(ranks))] for j in range(0, len(ranks))]; 

	#also need to transpose the give matrix
	for i in range(0, len(ranks)):
		#if a node as no outgoing connections, 
		#assign equal probability to go to every other node (1/n)
		if len(ranks[i]) == 0:
			for j in range(0, len(ranks)):
				matrix[j][i] = 1.0 / len(ranks);
		else:
			for j in range(0, len(ranks[i])):
				matrix[ranks[i][j]][i] = 1.0 / len(ranks[i]); #probability from one node to all other nodes


	#convert to a numpy matrix
	matrix = np.matrix(matrix);


	#(2) DO POWERMETHOD

	v = np.array([[1 for i in range(0, len(ranks))]]).transpose();

	#iterate until convergence or until 1000 iterations (so it doesn't take too long)
	numIterations = 0
	while(not np.array_equal(np.dot(matrix, v), v) and numIterations < 1000):
		v = np.dot(matrix, v);
		numIterations = numIterations + 1;

	
	#(3) CLEAN UP THE OUTPUT TO A SORTED (by index) PYTHON LIST

	#final vector is the result
	v = np.argsort(v.flatten()); #sort in asceding order
	v = list(reversed(v.tolist()[0])); #reverse to descending order

	#done
	return v;
