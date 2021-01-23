from cassandra.cluster import Cluster

cluster = Cluster()
session = cluster.connect()

session.execute(
    "CREATE KEYSPACE if not exists club_raise WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 3};")
session.execute("USE club_raise;")

# 建user表
# session.execute("CREATE TABLE  if not exists user (user_name text PRIMARY KEY,user_balance int,user_count int,user_passwd text,user_phone_number text,user_recount int,user_renumber text);")



# # 增数据
# def add():
#     # ls = [3, 'userthree', '123456', '15665656565', 0, 0, '1003', 0]
#     session.execute("INSERT INTO user (user_id , user_name , user_passwd ,user_phone , user_balance ,user_count ,"
#                      " user_renumber, user_recount) VALUES ( %s ,%s ,%s ,%s ,%s ,%s , %s , %s );",ls)
#
# def delete():
#     pass


# ls = [3, 'userthree', '123456', '15665656565', 0, 0, '1003', 0]
# session.execute("INSERT INTO user (user_id , user_name , user_passwd ,user_phone , user_balance ,user_count ,"
#                 " user_renumber, user_recount) VALUES ( %s ,%s ,%s ,%s ,%s ,%s , %s , %s );",ls)
# #
# cur = session.execute("select * from user  ;")
#
# username = 'userone'
# userpasswd = '123456'
# # cur = session.execute("select * from user where user=" + username and "password=" + userpasswd";")
# cur.execute("select * from user where user_name= username and user_passwd=userpasswd;")
# cur.execute(";")

# cur = session.execute("select * from user where user="+request.args.get('user')+" and password="+request.args.get('password'))
# username = 'userone'
# userpasswd = '123456'
# session.execute("CREATE INDEX ON user (user_passwd);")



# ls = ['usero']
# ls1 = ['123456']
# ls3 = []
# test = 0
# us = session.execute("select * from user where  user_name = %s;", ls)
# ps = session.execute(" select * from user where  user_passwd =%s;", ls1)
# for i in us:
#     ls3.append(i)
#     print(i)
#
# if len(ls3) == 0:
#     print("1")
# else:
#     print("2")

#


def ressult(ls,ls1):
    text = 0
    lstest = []
    lstest1 = []
    us = session.execute("select * from user where  user_name = %s;", ls)
    ps = session.execute("select * from user where  user_phone_number = %s;", ls1)

    for i in us :
        lstest.append(i)

    for j in ps:
        lstest1.append(j)

    if len(lstest) == 0 and len(lstest1) == 0:
        return 0
    else:
        return 1

# if __name__ == '__main__':
#     ls = ["userone"]
#     ls1 = ["15555555555"]
#     print(ressult(ls, ls1))


# for i in us:
#     for j in ps:
#         if i and j:
#             print("yes")
#             break
# ls = [222, 'userfi', '123456', '16666666666']
# session.execute("INSERT INTO user ( user_id, user_name , user_passwd ,user_phone ) VALUES ( %s ,%s , %s , %s );", ls)

# print(cluster.metadata.keyspaces['club_raise'].tables['user'])




