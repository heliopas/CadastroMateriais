import mysql.connector
from mysql.connector import Error
import globalVar

global cursor, dbconn

def dbConnect():
    try:
        dbconn = mysql.connector.connect(
            host=globalVar.host,
            user=globalVar.user,
            password=globalVar.password,
            database=globalVar.database
        )
        if dbconn.is_connected():
            serverInfo = dbconn.get_server_info()
            serverVersion = dbconn.get_server_version()
            print('Conecção estabelecida-> ' + str(serverInfo) + str(serverVersion))
            cursor = dbconn.cursor()
    except Error as e:
        print('Erro durante conecção:' + e)


def dbClose():
    if dbconn.is_connected():
        try:
            cursor.close()
            dbconn.close()
            print('Conexão encerrada!!')
        except Error as e:
            print('Erro durante fechar conexão DB:' + e)


# create table cadastroMaterial(
# 	desc_produto varchar(255),
#     ns_produto varchar(255) not null,
#     qtda int not null,
#     valor float,
#     data_hora varchar(255),
#     tipo_produto varchar(255) not null,
#     Col_ext_1 varchar(255),
#     Col_ext_2 varchar(255),
# 	Col_ext_3 int,
#     Col_ext_4 int,
# 	Col_ext_5 float,
#     Col_ext_6 int,
#     ID_produto int not null,
#     primary key (ID_produto)
# );