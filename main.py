import simon.py

def AllUsersConnection(): 
    try: 
        return MC.connect(host = 'localhost', database='eqlaflix', user = 'root', password = 'g5gqwagr' )
    except:
        try: 
            return MC.connect(host = 'localhost', database='eqlaflix', user = 'root', password = 'python4life' )
        except:
            return MC.connect(host = 'localhost', database='eqlaflix', user = 'root', password = 'isaac' )