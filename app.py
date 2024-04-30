# Case Based Sudoku Program
# Final project for AI class 
# Toby Baker and Thomas Denvir
# 4/30/2024
from flask import Flask
import webbrowser

app = Flask(__name__)

@app.route("/")
def index():
    webbrowser.open('index.html')
    return()


if __name__ == "__app__":
    app.run('localhost', 8080)