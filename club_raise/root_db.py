from cassandra.cluster import Cluster

cluster = Cluster()
session = cluster.connect()

session.execute(
    "CREATE KEYSPACE if not exists club_raise WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 3};")
session.execute("USE club_raise;")

def ressult(ls,ls1):
    text = 0
    lstest = []
    lstest1 = []
    us = session.execute("select * from root where  root_name = %s;", ls)
    ps = session.execute("select * from root where  user_phone_number = %s;", ls1)

    for i in us :
        lstest.append(i)

    for j in ps:
        lstest1.append(j)

    if len(lstest) == 0 and len(lstest1) == 0:
        return 0
    else:
        return 1


ls = ["rootone", "12345678"]
session.execute("INSERT INTO root (root_name, root_passwd ) VALUES (  %s , %s );",ls)






