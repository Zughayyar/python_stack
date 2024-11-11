from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    count_strawberry = request.form['strawberry']
    count_raspberry = request.form['raspberry']
    count_apple = request.form['apple']
    first_name_from_form = request.form['first_name']
    last_name_from_form = request.form['last_name']
    student_id = request.form['student_id']
    total = int(count_apple) + int(count_strawberry) + int(count_raspberry)
    print("Charging", first_name_from_form, last_name_from_form ,"for" , total)


    return render_template("checkout.html", strawberry = count_strawberry , raspberry = count_raspberry , apple = count_apple , first = first_name_from_form , last = last_name_from_form , id = student_id, total = total)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    