from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '66990609'
app.config['MYSQL_DB'] = 'dbaluguel'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
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

if __name__ == '__main__':
    app.run()









"""
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '66990609'
app.config['MYSQL_DB'] = 'db'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
    __________________________________________________________________
    
    <HTML>
<BODY bgcolor="blue">
<form method="POST" action="">
    <center>
    <H1>Enter your details </H1> <br>
    First Name <input type = "text" name= "fname" /> <br>
    Last Name <input type = "text" name = "lname" /> <br>
    <input type = "submit">
    </center>
</form>
</BODY>
</HTML>
"""