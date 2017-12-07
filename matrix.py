'''
This program reads integers from a user specified input file into two 2D arrays (matricies).
The matricies are multipled together and the rows of the product matrix are sorted.
All the matricies are written to an output.txt file in the same directory as matrix.py.

@author Sean Brady
@version 1.0 11/11/2017
'''

inputFile = raw_input("Enter the input file location (/home/user/Documents/example.txt):")

numbers = []
inFile = open (inputFile, "r")
for line in inFile.readlines():
    for i in line.split():
        numbers.append(int(i))

length = len(numbers)
size = length/5

outFile = open('output.txt','w')

def create_matrix(m, n):
    return [[0]*n for _ in xrange(m)]

A = create_matrix(size, 5)
outFile.write('Matrix A:\n')
count = 0
for j in range(5):
	for i in range(size):
		A[i][j] = numbers[count]
		outFile.write(str(A[i][j]),)
		outFile.write(' ')
		count = count+1
	outFile.write('\n')

B = create_matrix(5, size)
outFile.write('\nMatrix B:\n')
count = 0
for j in range(size):
	for i in range(5):
		B[i][j] = numbers[count]
		outFile.write(str(B[i][j]),)
		outFile.write(' ')
		count = count+1
	outFile.write('\n')

C = create_matrix(5, 5)
outFile.write('\nA*B:\n')
count = 0
k = size
for j in range(5):
	for i in range(5):
		for k in range(size):
			C[i][j] = A[k][j] * B[i][k]
		outFile.write(str(C[i][j]),)
		outFile.write(' ')
		count = count + 1
	outFile.write('\n')

outFile.write('\nA*B Sorted:\n')
count = 0
k = size
for j in range(5):
	for i in range(5):
		for k in range(size):
			C[i].sort()
		outFile.write(str(C[i][j]),)
		outFile.write(' ')
		count = count + 1
	outFile.write('\n')