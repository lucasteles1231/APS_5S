import mysql.connector

def UserValidation(user, password):
    con = mysql.connector.connect(host='localhost', database='APS_Ambiental',user='root',password='root')
    if con.is_connected():
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM USUARIOS WHERE USUARIO = '{user}' AND SENHA = '{password}';")
        result = cursor.fetchall()
        print(result)
        print(len(result))

UserValidation('john.doe.inspect@gmail.com','123456')