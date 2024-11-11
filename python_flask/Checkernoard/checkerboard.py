### Assignment: Checkerboard
### Anas Zughayyat

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def play():
    return render_template("index.html")

@app.route('/4')
def play_4():
    return render_template("index_4.html")

@app.route('/<x>/<y>')
def play_x_y(x,y):
    return render_template("index_x_y.html", x = int(x), y = int(y))

@app.route('/<x>/<y>/<color1>/<color2>')
def play_x_y_color(x,y, color1, color2):
    return render_template("index_x_y_color_color.html", x = int(x), y = int(y), color1 = color1, color2 = color2)

if __name__ == "__main__":
    app.run(debug=True)
