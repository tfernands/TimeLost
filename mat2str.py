import math
import random

n, m = 5, 5
mat = []

for i in range(n):
	mat.append([])
	for j in range(m):
		mat[i].append((random.random()-0)*1) 

def mat2str(mat: list, dec: int = 1, sw: int = 3, sh: int = 1, pdw: int = None, pdh: int = None) -> str:
	"""
	Generate a cool string representation of the matrix.
	
	Keyword arguments:
	mat: list[list[int]] -- the matrix
	dec: int             -- number of decimal places
	sw:  int             -- spaces between columns
	sh:  int             -- spaces between rows
	pdw: int             -- border padding width
	pdh: int             -- border parddin height
	return: str          -- string representation of the matrix
	"""
	maxn = maxc1 = 0
	for row in mat:
		maxc1 = max(maxc1, len(('{:.'+str(dec)+'f}').format(row[0])))
		for n in row:
			maxn = max(maxn, len(('{:.'+str(dec)+'f}').format(n)))
	pdw = (math.ceil(sw/2) if len(mat[0]) > 1 else 1) if pdw is None else pdw
	pdh = math.ceil((sh+0.6)/2) if pdh is None else pdh
	emptyc = (maxn*(len(mat[0])-1)+maxc1+pdw*2)+sw*(len(mat[0])-1)
	smat = '\u250C'+'\u2500'*pdw+(emptyc-pdw*2)*' '+'\u2500'*pdw+\
	'\u2510\n'+('\u2502'+emptyc*' '+'\u2502\n')*(pdh-1) if pdh > 0 else ''
	for i in range(len(mat)):
		smat += '\u2502'+' '*pdw
		for j in range(len(mat[i])):
			smat += ('{:'+str(maxc1 if j==0 else maxn)+'.'+str(dec)+'f}').format(mat[i][j])
			smat += ' '*sw if j < len(mat[0])-1 else ' '*pdw
		smat += '\u2502\n'+('\u2502'+emptyc*' '+'\u2502\n')\
		*sh if sh > 0 and i < len(mat)-1 else '\u2502\n'
	smat += ('\u2502'+emptyc*' '+'\u2502\n')*(pdh-1)+'\u2514'+\
	'\u2500'*pdw+(emptyc-pdw*2)*' '+'\u2500'*pdw+'\u2518\n' if pdh > 0 else ''
	return smat
	
print('')
print(mat2str(mat,10, sh=4))
