from flask import Flask, render_template, request, jsonify
import json
from flask_mysqldb import MySQL
app = Flask(__name__)

#  configuração do banco
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'teste'

mysql = MySQL(app)

#  cadastro de aluguel
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "POST":
        details = request.form
        id = details['id']
        livro = details['liv']
        situacao = details['sit']
        rent = details['aluguel']
        returnadate = details['dev']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(id, livro, situacao, rent, returnadate) VALUES (%s, %s, %s, %s, %s)", (id, livro, situacao, rent, returnadate))
        mysql.connection.commit()
        cur.close()
        return 'Cadastrado com sucesso.'
    return render_template('index.html')

#  listar todos
@app.route('/cads', methods=['GET'])
def home():
    if request.method == "GET":
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users;")
        json_string = cur.fetchall()
        return jsonify(json_string)

#  deletar cadastro pelo id
@app.route('/cads/<string:id>', methods=['DELETE'])
def remove_cad(id):
    if request.method == "DELETE":
        cur = mysql.connection.cursor()
        sql = "DELETE FROM users WHERE id='" + id + "'"
        cur.execute(sql)
        mysql.connection.commit()
        cur.close()
        return "Deletado com sucesso"

    else:
        return "Cadastro nao encontrado. Tente novamente."

#  editar a situação (disponivel ou alugado), o nome do solicitante e a data de devolução via id
@app.route('/cads/<string:id>', methods=['PUT'])
def edit_cad(id):
    if request.method == "PUT":
        cur = mysql.connection.cursor()
        sql = "UPDATE users SET situacao='"+ request.get_json().get('situacao') +"', rent='" + request.get_json().get('rent') + "', returnadate='" + request.get_json().get('returnadate') +"'WHERE id='" + id + "'"
        cur.execute(sql)
        mysql.connection.commit()
        cur.close()
        return "Editado com sucesso"
    else:
        return "Erro ao editar. Tente novamente."


if __name__ == '__main__':
    app.run()