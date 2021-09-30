from simon import *

def AllUsersConnection(): 
	try: 
		return MC.connect(host = 'localhost', database='score', user = 'root', password = 'g5gqwagr' )
	except:
		try: 
			return MC.connect(host = 'localhost', database='score', user = 'root', password = 'python4life' )
		except:
			try: 
				return MC.connect(host = 'localhost', database='score', user = 'root', password = 'elochat' )
			except:
				try: 
					return MC.connect(host = 'localhost', database='score', user = 'root', password = 'eleochat' )
				except:
					try: 
						return MC.connect(host = 'localhost', database='score', user = 'root', password = 'Eleochat' )
					except:
						try:
							return MC.connect(host = 'localhost', database='score', user = 'root', password = 'isaac' )
						except:
							try:          
								return MC.connect(host = 'localhost', database='score', user = 'root', password = '@Mcyber66' )
							except:
								print("Erreur de connexion...")

cnx = AllUsersConnection()
