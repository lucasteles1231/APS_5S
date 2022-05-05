import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

@app.route('/dadosDBAPI')
def dadosDBAPI():
    con = mysql.connector.connect(host='localhost', database='MYSQL_PYTHON',user='root',password='root')
    if con.is_connected():
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM Tabela_Dados")
        result = cursor.fetchall()
        data = {
            'ID': [],
            'NOME': [],
            'SOBRENOME': [],
            'APELIDO': [],
            'EMAIL': [],
            'CPF': []
            }

        for i in result:
            data['ID'].append(i[0])
            data['NOME'].append(i[1])
            data['SOBRENOME'].append(i[2])
            data['APELIDO'].append(i[3])
            data['EMAIL'].append(i[4])
            data['CPF'].append(i[5])
        
        return jsonify(data)

app.run(host='0.0.0.0')