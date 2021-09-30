import datetime
import mysql.connector as MC

def GetConnection(): 
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
								return MC.connect(host = 'localhost', database='supersimon', user = 'root', password = '@Mcyber66s' )
							except MC.Error as error:
								raise Exception(f"Connexion à la DB:{error}")

def PrintScore():
	try:
		cnx = GetConnection()
		curseur = cnx.cursor()
		curseur.execute("select * from score ORDER BY score DESC Limit 10")
		tousLesEnregistrements = curseur.fetchall()
		for enregistrement in tousLesEnregistrements:
			print("date et heure: ", enregistrement[3], "nom:", enregistrement[1], "score: ", enregistrement[2])
		curseur.close()
		cnx.close()
	except Exception as erreur:
		#print("Une erreur est survenue:", erreur)
		raise Exception(erreur)

def AddScore(_name, _score):
	try:
		cnx = GetConnection()
		curseur = cnx.cursor()
		dayTime = datetime.datetime.now() 
		requete = f"INSERT INTO score(pseudo,  score, datescore) VALUES ('{_name}', {_score}, '{dayTime}');"
		curseur.execute(requete)
		cnx.commit()

		curseur.close()
		cnx.close()
	except Exception as erreur:
		#print("Une erreur est survenue:", erreur)
		raise Exception(erreur)
