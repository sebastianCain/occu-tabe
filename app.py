from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")

def route1():
	return render_template("index.html", title = "This be the first page")

@app.route("/occu")

def route2():
	return render_template("occu.html", title = "this is the second route.")

def getOccuData():
    occu = open("occupations.csv", "r")
    streamy = occu.read()

    data = streamy.strip().split("\n")

    for line in range(len(data)):
        line.strip('"')

if __name__ == "__main__":
    app.debug = True
    app.run()
