from simon import *
#import mysql.connector as MC


def AllUsersConnection(): 
	try: 
		return MC.connect(host = 'localhost', database='supersimon', user = 'root', password = 'g5gqwagr' )
	except:
		try:
			return MC.connect(host = 'localhost', database='supersimon', user = 'root', password = 'python4life' )
		except:
			try:
				return MC.connect(host = 'localhost', database='supersimon', user = 'root', password = 'elochat' )
			except:
				try:
					return MC.connect(host = 'localhost', database='supersimon', user = 'root', password = 'eleochat' )
				except:
					try: 
						return MC.connect(host = 'localhost', database='supersimon', user = 'root', password = 'Eleochat' )
					except:
						try:
							return MC.connect(host = 'localhost', database='supersimon', user = 'root', password = 'isaac' )
						except:
							try:          
								return MC.connect(host = 'localhost', database='supersimon', user = 'root', password = '@Mcyber66' )
							except:
								print("Erreur de connexion...")


def PrintScore():
	cnx = AllUsersConnection()
	try:
		curseur = cnx.cursor()
		curseur.execute("select * from score")
		donnees = curseur.fetchall()
		for enregistrement in donnees:
			#print("Idscore: ", enregistrement[0], "nom: ", enregistrement[1], "score: ", enregistrement[2])
			print("nom:", enregistrement[1], "score: ", enregistrement[2])
		curseur.close()
		cnx.close()
	except Exception as erreur:
		print("Une erreur est survenue:", erreur)

def AddScore(_name, _score):
	cnx = AllUsersConnection()
	try:
		curseur = cnx.cursor()
		requete = f"INSERT INTO score(pseudo,  score, datescore) VALUES ('{_name}', {_score}, '2021/12/12');"
		print(requete)
		curseur.execute(requete)
		cnx.commit()

		curseur.close()
		cnx.close()
	except Exception as erreur:
		print("Une erreur est survenue:", erreur)





AddScore(SimonNamePlayer, newPlayerPoint)
PrintScore()