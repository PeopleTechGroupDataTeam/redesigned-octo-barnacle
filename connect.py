import pyodbc
import logging

server = '127.0.0.1'
database = 'master'
username = 'sa'
password = 'Banana1000'
cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';P'
                                                                                                               'WD=' + password)
cursor = cnxn.cursor()

#cursor_new = cnxn.cursor()
def validate():
    result = []
    with open('/Users/saisiddharthavungarala/PycharmProjects/SQL_Validation/insert_1.txt', 'r') as inserts:
        query = inserts.read().split("\n")
        for i, j in enumerate(query):
            cursor.execute(j)
            #cursor_new.execute(j)

            get_length = cursor.fetchone()
            #get_length_new = cursor_new.fetchone()
            result.append(get_length[0])
        return result

#  Without  Loop
'''
query_1 = "SELECT COUNT(*) FROM Products"
print(type(query_1))                                         # <class 'str'>
cursor.execute(query_1)
get_length = cursor.fetchone()
print(get_length[0])                                        #  77
'''

print(validate())


'''
if get_length[0] == 3:
    mylogger.warning("Passsed")
else:
    mylogger.warning("Failed")
'''
