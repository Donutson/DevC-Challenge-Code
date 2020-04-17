#------------------------------------------------------------------------------
# Name:        deminer
# Purpose:		resolution du challenge code organise par
#				Facebook Develoer Circle Abidjan dans la periode du 2020/04/[15-19]
#
# Author:      Nelson
#
# Created:     16/04/2020
# Copyright:   (c) HP 2020
# Licence:     Creative commons
#-------------------------------------------------------------------------------
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def deminer(n, m, champ, point):
	x, y = point
	coordvoisins = [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]
	nbmine = 0
	for a, b in coordvoisins:
		if (a in range(n)) and b in range(m):
			if champ[a][b] == '*':
				nbmine += 1
	return nbmine

def deminersolve(n,m,champ):
	champr = [['.']*m for i in range(n)]
	for i in range(n):
		for j in range(m):
			if champ[i][j] != '*':
				champr[i][j] = deminer(n, m, champ, (i,j))
			else:
				champr[i][j] = '*'
	return champr

def main():
	
	n, m = list(map(int, sys.argv[1:3]))
	i = 0
	ligne = []
	champ = []
	for el in sys.argv[3:4+m*n]:
		ligne.append(el)
		i += 1
		if i%m == 0:
			champ.append(ligne)
			ligne = []

	champ = deminersolve(n,m, champ)

	# affichage de la sortie
	for el in champ:
		for case in el:
			print(case, end='')
		print()

main()