###########################
### Python Stack: Flask ###
###########################
##### Anas Zughayyar ######
###########################
### Assignment: Counter ###
###########################

from flask import Flask, render_template, request, redirect , session
app = Flask(__name__)  
app.secret_key = "keep it secret"


@app.route('/')
def landing_page():
    if 'count_visit' in session:
        session['count_visit'] += 1
    else:
        session['count_visit'] = 0
    return render_template("index.html")

@app.route('/destroy_session')
def destroy_session():
    if 'count_visit' in session:
        session['count_visit'] = 0
    return render_template("index.html")

if __name__=="__main__":   
    app.run(debug=True)    
