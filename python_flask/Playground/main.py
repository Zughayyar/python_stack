### Assignment: Playground
### Anas Zughayyat

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template("index.html")

@app.route('/play/<x>')
def play_x(x):
    return render_template("play_x.html", x = int(x))

@app.route('/play/<x>/<color>')
def play_x_color(x,color):
    return render_template("play_x_color.html", x = int(x), color = color)

if __name__ == "__main__":
    app.run(debug=True)
