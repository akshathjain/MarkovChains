#Name: Akshath Jain
#Date: 11/25/18
#Purpose: spectral clustering algorithm for 21241 final project

import numpy as np;

#main function
def main():
	adjList = [[1, 2],[0],[],[1, 2]];
	x = rank(adjList);	
	print(x);

#does the heavy lifting
def rank(ranks):

	#=========================================
	#(1) CREATE MATRIX REPRESENTING PAGE LINKS
	#=========================================

	#initialize nxn matrix full of zeros
	M = [[0 for i in range(0, len(ranks))] for j in range(0, len(ranks))]; 

	#also need to transpose the give matrix
	for i in range(0, len(ranks)):
		#if a node as no outgoing connections, 
		#assign equal probability to go to every other node (1/n)
		if len(ranks[i]) == 0:
			for j in range(0, len(ranks)):
				M[j][i] = 1.0 / len(ranks);
		else:
			for j in range(0, len(ranks[i])):
				M[ranks[i][j]][i] = 1.0 / len(ranks[i]); #probability from one node to all other nodes

	M = np.matrix(M);


	#------------------------------
	#(1A) HANDLING REDUCIBLE GRAPHS
	#------------------------------

	#convert to a numpy matrix
	O = np.matrix([[1 for i in range(0, len(ranks))] for j in range(0, len(ranks))]); # nxn matrix full of ones
	d = 0.15 #standard value for damping factor, (will change answers for test case)
	M = d * M + (1.0 - d) / len(M) * O; #dampen M



	
	#==================
	#(2) DO POWERMETHOD
	#==================

	v = np.array([[1 for i in range(0, len(ranks))]]).transpose();

	#iterate until convergence or until 1000 iterations (so it doesn't take too long)
	numIterations = 0
	while(not np.array_equal(np.dot(M, v), v) and numIterations < 1000):
		v = np.dot(M, v);
		numIterations = numIterations + 1;

	


	#==========================================================
	#(3) CLEAN UP THE OUTPUT TO A SORTED (by index) PYTHON LIST
	#==========================================================

	#final vector is the result
	sort = np.argsort(v.flatten()); #sort in asceding order
	sort = list(reversed(sort.tolist()[0])); #reverse to descending order

	#fin.
	return sort;
