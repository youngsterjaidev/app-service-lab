from flask import Flask, request

import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
  host="app-service-db.mysql.database.azure.com",
  user="myadmin@app-service-db",
  password="ankit#123",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


@app.route("/")
def hello_world():
    return "<p>This is a App Service running in vm</p>"

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        print(username, email, password)

        return "<p>Data is inserted!<p>"


    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return "<p>Please send post request<p>"

if __name__ == "__main__":
    app.run(debug=True)
