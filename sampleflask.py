from flask import Flask

sampleflask = Flask(__name__) 

@sampleflask.route("/")
def home():
    return '''Do you like cats or dogs more? <br>
<a href="http://127.0.0.1:5000/cats">Cats</a>
<a href="http://127.0.0.1:5000/dogs">Dogs</a>'''

@sampleflask.route("/cats")
def cat():
    return '''The choice is obvious. Cats are purrfect.<br>
<a href="http://127.0.0.1:5000/">Change your mind?</a>'''

@sampleflask.route("/dogs")
def dog():
    return '''This shouldn't be a pawblem. Dogs are the best.<br>
<a href="http://127.0.0.1:5000/">Change your mind?</a>'''

if __name__ == "__main__":
    sampleflask.run()
