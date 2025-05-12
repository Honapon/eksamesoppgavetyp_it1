from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

#connect to database
mydb = mysql.connector.connect(
  host="172.28.110.89",
  user="flaks",
  password="Passord",
  database="hoytorptreffet"
)

def db_connection():
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except Error as e:
        print(f"Error connecting to mariadb: {e}")
        return None

@app.route('/')
def index():
    return render_template ("index.html")

@app.route('/registrer.html')
def registrer():
    return render_template("registrer.html")
@app.route('/submit_reg', methods=['POST'])
def submit_reg():
    #tar input fra form. 
    

if __name__ == "__main__":
    app.run(debug=True)
    