from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>This is a App Service app</p>"

if __name__ == "__main__":
    app.run(debug=True)
