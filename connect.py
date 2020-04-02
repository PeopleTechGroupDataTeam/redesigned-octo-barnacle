import pyodbc

server = '127.0.0.1'
database = 'master'
username = 'sa'
password = 'Banana1000'
connect = pyodbc.connect(
                    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';P'
                                                                                                               'WD=' + password)
cursor = connect.cursor()

def validate():
    result = []
    with open('/Users/saisiddharthavungarala/PycharmProjects/SQL_Validation/insert.txt', 'r') as inserts:
        query = inserts.read().split("\n")
        for i, j in enumerate(query):
            cursor.execute(j)
            #cursor_new.execute(j)

            get_length = cursor.fetchone()
            #get_length_new = cursor_new.fetchone()
            result.append(get_length[0])
        return result

print(validate())


