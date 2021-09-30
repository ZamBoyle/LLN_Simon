from DAL import *
import random
import sys
import os
import time
player_point = 0
lifeplayerlevel2 = 3
lifeplayerlevel3 = 5
nameBoard=["SimonDad","Simonmom","SimonSon","SimonSister","SimonBaby"]
scoreBoard=[5,4,3,2,1]

def SuperSimonEndinScreenError():
	print("oops, tu t'es trompé! \n Et si tu faisais une cure de poisson pour améliorer ta mémoire? \n Allez, ne te décourages pas, la mémoire !ça se travaille \n Reviens vite!!!")

def increasepoint(player_point):
		player_point+=1
		print("tu gagnes un point tu en as " + str(player_point))
		return player_point
		
def withdraw(player_point):
	player_point-=1
	print(" tu prds un point de vie, tu en as "  + str(player_point))
	return player_point

def newLifePoint (lifeplayerlevel2):
	lifeplayerlevel2 -=1
	print(" tu perds un point de vie, tu en as "  + str(lifeplayerlevel2))
	return lifeplayerlevel2

def newLifePoint (lifeplayerlevel3):
	lifeplayerlevel3 -=1
	print(" tu perds un point de vie, tu en as "  + str(lifeplayerlevel3))
	return lifeplayerlevel3

color = ["bleu", "jaune", "rouge", "vert"]
colorRandomGenerated = []

def colorRandom(color):
	newColor = random.choice(color)
	if len(colorRandomGenerated) > 2:
		while newColor == colorRandomGenerated[-1]   == colorRandomGenerated[-2]:
			newColor = random.choice(color)
	return newColor

def newColorGenerated():
	colorRandomGenerated.append(colorRandom(color))
	print("la couleur choisie est ", colorRandomGenerated)
	time.sleep(2)
	os.system('cls')
("la couleur choisie est ", colorRandomGenerated)

def listCompare(_firstAnswer):
	if _firstAnswer == colorRandomGenerated :
		if len(colorRandomGenerated) != 0:
			print("bravo, tu as trouvé \n tu passes à l'étape suivante \n")
		return True
	else:
		print("dommage tu t'es trompé \n")
		return False

def answerPlayer():
	_colorPlayerAnswer= []
	for i in range (len(colorRandomGenerated)):
		userAnser = input("quel est la couleur "  + str(i+1) + "? \n" )
		if userAnser == "j":
			_colorPlayerAnswer.append("jaune")
		if userAnser == "b":
			_colorPlayerAnswer.append("bleu")
		if userAnser == "r":
			_colorPlayerAnswer.append("rouge")
		if userAnser == "v":
			_colorPlayerAnswer.append("vert")   
	return _colorPlayerAnswer

def mainLevel1(player_point):
	_userAnswer = []
	while listCompare(_userAnswer): 
		if _userAnswer != []:
			player_point = increasepoint(player_point)
		newColorGenerated()
		_userAnswer = answerPlayer()
		global newPlayerPoint
		newPlayerPoint = player_point
	else:
		print("Cette erreur te fait quitter le jeu, néanmoins tu as réussi à gagner " + str(player_point) + " points ")

def mainLevel2(player_point, lifeplayerlevel2):
	_userAnswer = []
	while lifeplayerlevel2 != 1: 
		if listCompare(_userAnswer) :
			if _userAnswer != []:
				player_point = increasepoint(player_point)
				global newPlayerPoint
				newPlayerPoint = player_point
			newColorGenerated()
		else:
			lifeplayerlevel2 = newLifePoint(lifeplayerlevel2)
			print("Cette fois çi essaie de les retenir \n Les couleurs sonts  ", colorRandomGenerated)
			time.sleep(2)
			os.system('cls')
		_userAnswer = answerPlayer()
	else:
		print(" Tu as perdu tes points de vies, le jeu s'arrête ici pour toi, reprends des vitamines, entraîne ta mémoire et reviens retenter ta chance \n ")

def mainLevel3(player_point, lifeplayerlevel3):
	_userAnswer = []
	while lifeplayerlevel3 != 1: 
		if listCompare(_userAnswer) :
			if _userAnswer != []:
				player_point = increasepoint(player_point)
				global newPlayerPoint
				newPlayerPoint = player_point
			newColorGenerated()
		else:
			lifeplayerlevel3 = newLifePoint(lifeplayerlevel3)
			print("Cette fois çi essaie de les retenir \n Les couleurs sonts  ", colorRandomGenerated)
			time.sleep(2)
			os.system('cls')
		_userAnswer = answerPlayer()
	else:
		print(" Tu as perdu tes points de vies, le jeu s'arrête ici pour toi, reprends des vitamines, entraîne ta mémoire et reviens retenter ta chance \n ")

def SuperSimonEndingScreenScoreBoard(newPlayerPoint):
	for i  in range(len(nameBoard)):
		if newPlayerPoint >= scoreBoard[i]:
			scoreBoard.insert(i,newPlayerPoint)
			nameBoard.insert(i,SimonNamePlayer)
			# print(scoreBoard)
			# print(nameBoard)
			break
	else:
		print("Vous n'avez pas obtenu assez de points pour être classé \n")

def printScoreBoard(newPlayerPoint):
	for i in range (len(scoreBoard)):
		print(str(nameBoard[i]) + " a " + str(scoreBoard[i]) + " points " )

def startScreen():
	print("Bonjour et bienvenu dans notre Super Simon \n")
	print("Nous te proposons te tester ta mémoire \n")
	print("Les couleurs suivantes vont t'être proposées de façon aléatoire : bleu, jaune, rouge et vert. \n Il te suffit de les reproduire grâce à ton clavier. \n pour cela, il te suffit d'inscrire l'initiale de la couleur \n b pour bleu \n j pour jaune \n r pour rouge \n v pour vert \n")
	print("On commence par une couleur, et à chaque bonne réponse, il y en aura une supplémentaire avec des points bonus à la clé \n")
	print("A toi de jouer, prépare tes neurones \n")

	SimonPlayer=input(("Pour commencer le jeu, appuye sur \n y  \n ou \n n pour quitter\n"))

	if SimonPlayer == "y":
		global SimonNamePlayer
		SimonNamePlayer=input("Choisis maintenant un surnom ou tout simplement ton prénom \n")
		print("bienvenu " +  SimonNamePlayer + " , maintenant je te propose de choisir ton niveau de jeu \n")
		print("Tu as le choix entre 3 niveaux de jeu \n Le premier où tu n'as pas le droit à l'erreur \n Le second où tu bénéficie de 3 points de vies \n Le troisième où tu bénéficies de 5 points de vies")
		levelChoice =int(input("Choisis entre \n 1 \n 2 \n 3 \n pour choisir ton niveau\n"))
		if levelChoice == 1:
			print("Attention, la moindre erreur te feras perdre \n Ta concentration doit être totale \n")
			mainLevel1(player_point)
		elif levelChoice== 2:
			print("C'est parti pour le 2ème niveau, tu commences avec " + str(lifeplayerlevel2) + " points de vies ")
			mainLevel2(player_point, lifeplayerlevel2)  
		elif levelChoice== 3:
			print("C'est parti pour le 3ème niveau, tu commences avec " + str(lifeplayerlevel3) + " points de vies ")
			mainLevel3(player_point, lifeplayerlevel3)
		else:
			print("ton choix n'est pas bon, ce niveau n'existe pas \n")
	else:
		exit()

try:
	while True:
		PrintScore()
		startScreen()
		SuperSimonEndingScreenScoreBoard(newPlayerPoint)
		#printScoreBoard(newPlayerPoint)
		AddScore(SimonNamePlayer, newPlayerPoint)
		PrintScore()
except Exception as erreur:
	print(f"Une erreur est survenue:{erreur}")
