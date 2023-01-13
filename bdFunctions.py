import mysql.connector
import messagePipe
from mysql.connector import Error
from files import globalVar

global cursor, dbconn

# create table cadastroMaterial(
# 	    desc_produto varchar(255),
#       ns_produto varchar(255) not null,
#       qtda int not null,
#       valor float,
#       data_hora varchar(255),
#       tipo_produto varchar(255) not null,
#       Col_ext_1 varchar(255),           // Tabela para registro de emprestimo
#       Col_ext_2 varchar(255),
# 	    Col_ext_3 int,
#     Col_ext_4 int,
# 	Col_ext_5 float,
#     Col_ext_6 int,
#     ID_produto int not null,
#     primary key (ID_produto)
# );

dbStringInsert = 'INSERT INTO cadastroMaterial(desc_produto, ns_produto, qtda, valor, data_hora, ' \
                 'tipo_produto, Col_ext_1, Col_ext_2, Col_ext_3, Col_ext_4, Col_ext_5, ' \
                 'Col_ext_6, ID_produto) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'

dbGetTableDataOR = 'SELECT * FROM cadastroMaterial where ns_produto = (%s) or tipo_produto = %s;'
dbGetTableDataAND = 'SELECT * FROM cadastroMaterial where ns_produto = (%s) and tipo_produto = %s;'

dbDeleteData = 'DELETE FROM cadastroMaterial where ns_produto = (%s) or ID_produto = (%s);'

dbUpdateName = 'UPDATE cadastroMaterial set Col_ext_1 = (%s) where ID_produto = (%s);'


#val = [('Medidor E223', '4N234514', '5', '17.895', '27/12/2025 - 12:45 AM', 'Cabo', '3', '2', '1', '3', '2', '1', '2231422')]

def dbConnect():
    global dbconn, cursor
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
            return 0
    except Error as e:
        print('Erro durante conecção:' + e)
        return 1

def dbClose():
    if dbconn.is_connected():
        try:
            cursor.close()
            dbconn.close()
            #messagePipe.messageInfo('Conexão BD fechada!')
        except Error as e:
            messagePipe.messageError('BD error: '+ str(e))

def dbInsert(value):
    dbConnect()
    if dbconn.is_connected():
        try:
            cursor.executemany(dbStringInsert, tuple(value))
            dbconn.commit()
            messagePipe.messageInfo('Intem inserido com sucesso!!!')
        except Error as e:
            messagePipe.messageError('BD error: '+ str(e))
    dbClose()

def dbGetData(ns, prodType):
    dbConnect()
    if dbconn.is_connected():
        try:
            if (ns and prodType) != '':
                cursor.execute(dbGetTableDataAND, (ns, prodType))
            else:
                cursor.execute(dbGetTableDataOR, (ns, prodType))
            receivedData = cursor.fetchall()
            print(receivedData)
        except Error as e:
            messagePipe.messageError('BD error: ' + str(e))
    dbClose()

    return receivedData

def dbDelete(ns, ID_produto):
    dbConnect()
    if dbconn.is_connected():
        if (ns and ID_produto) != '':
            try:
                cursor.execute(dbDeleteData, (ns, ID_produto))
                dbconn.commit()
                messagePipe.messageInfo('Apagado com sucesso!!!')
            except Error as e:
                messagePipe.messageError('BD error: ' + str(e))
    dbClose()

def dbUpdateData(name, ID_produto):
    dbConnect()
    if dbconn.is_connected():
        if (name and ID_produto) != '':
            try:
                cursor.execute(dbUpdateName, (name, ID_produto))
                dbconn.commit()
                messagePipe.messageInfo('Emprestimo registrado!!!')
            except Error as e:
                messagePipe.messageError('BD error: ' + str(e))
    dbClose()



