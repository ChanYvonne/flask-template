from flask import Flask

app = Flask(__name__) 

@app.route("/")
def home():
    return "Do you like cats or dogs more?"

@app.route("/cats")
def cat():
    return "The choice is obvious. Cats are purrfect."

@app.route("/dogs")
def dog():
    return "This shouldn't be a pawblem. Dogs are the best."


if __name__ == '__main__':
    app.run()
