from flask import Flask, render_template, request
from flask_mysqldb  import MySQL

app = Flask(__name__)

# mengatur database mysql
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskdb'
mysql = MySQL(app)


@app.route("/mhs")
def data_mhs():
    #membuka ccursor untuk mengeksekusi query mysql
    curr = mysql.connection.cursor()
    curr.execute("SELECT * FROM mahasiswa")
    data = curr.fetchall()
    curr.close()
    print("Data database: ", data)
    return render_template("mhs.html", data=data)

@app.route("/")
def helloWorld():
    return "<p>Hello World</p>"

@app.route("/about")
def about():
    return "<p>Ini about</p>"



if __name__ == "__main__":
    app.run(debug=True)