
from flask import Flask, render_template, request

app = Flask(__name__);

@app.route("/", methods=['GET'])
def whyTho():
    default = '0'
    return render_template('testforms.html')


@app.route("/auth")
def authenticate():
    print(app)
    print(request)
    print(request.args)
    return("AHHHHHHH")
    # page = open("renstart.html", "r")
    # html = page.read()


if __name__ == "__main__":
    app.debug = True
    app.run();

