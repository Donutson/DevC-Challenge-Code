#-------------------------------------------------------------------------------
# Name:        lcdshow
# Purpose:		resolution du challenge code organise par
#				Facebook Develoer Circle Abidjan dans la periode du 2020/04/[22-26]
#
# Author:      Nelson
#
# Created:     22/04/2020
# Copyright:   (c) HP 2020
# Licence:     Creative commons
#-------------------------------------------------------------------------------
#!/usr/bin/env python

class Numbers:
	"""
		Cette classe permet de créer en format lcd des nombres allant de 0 à 9
	"""

	def zero(s):

		hor = ' ' + '-'*s + ' '
		ver = ('|' + ' '*s + '|\n')*s

		return hor + '\n' + ver + '\n' + ver + hor +'\n'

	def one(s):

		hor = ' '*(s+2)+'\n'
		ver = ('  |'+' '*(s-1)+'\n')*s

		return hor + ver + hor +ver+hor

	def two(s):

		hor = ' '+'-'*s+' \n'
		ver1 = (' '*(s+1)+'|\n')*s
		ver2 = ('|'+' '*(s+1)+'\n')*s

		return hor + ver1 + hor + ver2 + hor

	def three(s):

		hor = ' '+'-'*s+' \n'
		ver = (' '*(s+1)+'|\n')*s
		
		return hor + ver + hor + ver + hor

	def four(s):

		edge = ' '*(s+2)+'\n'
		ver1 = ('|'+' '*s+'|\n')*s+' '+'-'*s+' \n'
		ver2 = (' '*(s+1)+'|\n')*s

		return edge + ver1 + ver2 + edge

	def five(s):

		hor = ' '+'-'*s+' \n'
		ver2 = (' '*(s+1)+'|\n')*s
		ver1 = ('|'+' '*(s+1)+'\n')*s

		return hor + ver1 + hor + ver2 + hor
		
	def six(s):

		 hor = ' '+'-'*s+' \n'
		 ver1 = ('|'+' '*(s+1)+'\n')*s
		 ver2 = ('|'+' '*s+'|\n')*s

		 return hor + ver1 + hor + ver2 +hor

	def seven(s):

		hor = ' '+'-'*s+' \n'
		ver = (' '*(s+1)+'|\n')*s

		return hor + ver + ' '*(s+2) + '\n' + ver + ' '*(s+2) + '\n'

	def eight(s):

		hor = ' '+'-'*s+' \n'
		ver = ('|'+' '*s+'|\n')*s

		return hor + ver + hor + ver + hor

	def nine(s):

		hor = ' '+'-'*s+' \n'
		ver1 = ('|'+' '*s+'|\n')*s
		ver2 = (' '*(s+1)+'|\n')*s

		return hor + ver1 + hor + ver2 + hor 

	@staticmethod
	def getnumber(number, s):
		"""
			Cette methode nous retourne le nombre s en format lcd
		"""

		if number == 0:
			return Numbers.zero(s)

		if number == 1:
			return Numbers.one(s)

		if number == 2:
			return Numbers.two(s)

		if number == 3:
			return Numbers.three(s)

		if number == 4:
			return Numbers.four(s)

		if number == 5:
			return Numbers.five(s)

		if number == 6:
			return Numbers.six(s)

		if number == 7:
			return Numbers.seven(s)

		if number == 8:
			return Numbers.eight(s)

		if number == 9:
			return Numbers.nine(s)

def showlcd(s, n):
	"""
		Cette fonction génère l'affichage du nombre n
		en format lcd avec une dimension de s
	"""

	schema = []
	nbrows = 2*s + 3
	nbdigits = len(str(n))
	screen = ''

	#creation du squelette de l'affichage
	for digit in str(n):

		number = Numbers.getnumber(int(digit), s)
		number = number.split('\n')
		number.pop()

		schema.append(number)

	#creation de l'affichage
	for i in range(nbrows):
		for j in range(nbdigits-1):
			screen += schema[j][i] + ' '

		screen += schema[nbdigits-1][i] + '\n'
	
	print(screen)

def main():

	s, n = list(map(int, input().split(' ')))

	while s != 0 and n != 0:
		
		showlcd(s,n)
		s, n = list(map(int, input().split(' ')))

if __name__ == '__main__':
	main()
