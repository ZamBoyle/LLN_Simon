import datetime
import mysql.connector as MC

#Il y a 7 étapes pour effectuer des requêtes dans MySql
#
#1. Création d'une connection (connect)
#2. Création d'un curseur à partir de la connexion créee
#3. Création d'une chaîne de requête
#4. Exécution (execute) de la requête à partir du curseur
#5. Valider (Commit) la requête, de la transaction en cours, pour des requêtes de type: INSERT, UPDATE, DELETE, etc. Pas pour un SELECT.
#6. Fermer (close) le curseur
#7. Fermer (close) la connexion

def GetConnection(): 
	"""Cette fonction crée et retourne un objet de type MysqlConnection
 
	Vu que nous avons presque tous des mots de passes différents, on va effectuer une succession de try except.
	En effet quand une connexion échoue, on réessaie avec un autre mot de passe."""
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
							except MC.Error as error:
								raise Exception(f"Connexion à la DB:{error}")

def PrintScore():
	"""Fonction qui affiche les scores stockés en DB"""
	try:
		#On reçoit un object de type MySQLConnection de la fonction GetConnection()
		cnx = GetConnection()
  		#A partir de la connexion, on crée un objet de type MysqlCursor. La méthode cursor() de l'objet cnx crée un curseur.
  		#Un curseur va interagir avec notre notre connexion établie au serveur MySql. Le curseur permettra d'exécuter des requêtes SQL.
		curseur = cnx.cursor()
  		#Execute la requete
		curseur.execute("select * from score ORDER BY score DESC Limit 10")
  		#On récupère tous les enregistrement (fetchall) dans la variables tousLesEnregistrements
		tousLesEnregistrements = curseur.fetchall()
  		#On va parcourir tous nos enregistrements.
  		#L'enregistrement en cours est stocké dans la variable enregistrement
		for enregistrement in tousLesEnregistrements:
			#On affiche le résultat. On prend dans le tableau, le champ à l'indice 1 (nom), l'indice 2 (score), l'indice 3 (date)
			print(f"date et heure: {enregistrement[3]} nom: {enregistrement[1]} score: {enregistrement[2]}")
  		#On ferme le curseur
		curseur.close()
  		#On ferme la connection
		cnx.close()
	except Exception as erreur:
		print("Une erreur est survenue:", erreur)

def AddScore(_name, _score):
	"""Fonction qui ajoute un score en DB
 	
  	_name -- nom du joueur (str)
   	_score -- score obtenu par le joueur (int)
  	"""
	try:
		cnx = GetConnection()
		curseur = cnx.cursor()
		dayTime = datetime.datetime.now() 
		requete = f"INSERT INTO score(pseudo,  score, datescore) VALUES ('{_name}', {_score}, '{dayTime}');"
  		#Attention si quelqu'un entre pour _name= la valeur ==> johnny',1000,'2021/10/1'); #
		print(requete)
		curseur.execute(requete)
  		#On commit/valide notre requête d'insertion de la transaction en cours.
		cnx.commit()

		curseur.close()
		cnx.close()
	except Exception as erreur:
		print("Une erreur est survenue:", erreur)
