### Assignment: HTML Table
### Anas Zughayyat

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/table')
def table():
    
    users_table = [
        {'first_name': 'Michael' , 'last_name' : 'Choi'},
        {'first_name': 'John' , 'last_name' : 'Supsupin'},
        {'first_name': 'Mark' , 'last_name' : 'Guillen'},
        {'first_name': 'KB' , 'last_name' : 'Tonel'}
    ]
    return render_template('index.html', table = users_table)



if __name__=="__main__":
    app.run(debug=True)