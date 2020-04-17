import os
import subprocess
import shutil

def check(code, correction, file):
	"""
		Cette se charge de vérifier si le code du candidat
		est renvoie la bonne réponse, si c'est le cas on conserve son code
		sinon on le supprime et enregistre également son resultat
	"""

	reponse = subprocess.check_output(['python','codes/'+ code] + list("44*........*......0035**.........*...00"))
	reponse = reponse.decode('utf-8')
	
	if reponse == correction:
		print(code+': good', file=file)
		print(code+': good')
		shutil.move('codes/'+ code, 'traiter')
	else:
		print(code+': bad',file=file)
		print(code+': bad', file=file)
		os.remove('codes/'+ code)



if not os.path.exists('traiter'):
	os.mkdir('traiter')


correction = subprocess.check_output(['python','correction.py'] + list("44*........*......0035**.........*...00"))
correction = correction.decode('utf-8')

with open('resultats.txt','a') as file:
	for code in os.listdir('codes'):

		check(code,correction,file)