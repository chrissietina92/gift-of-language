from flask import Flask, jsonify, request, render_template
from db_functions import add_a_new_user

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    clicked = False
    if request.method == 'POST':
        clicked = True
        form = request.form
        get_login_details(form)
        # print(form) #ImmutableMultiDict([('logintype', 'u'), ('username', 'hi'), ('password', 'Chrissie'), ('next', 'Next')])
    return render_template('login.html', clicked = clicked)

def get_login_details(form):
    chosen_log_in = form['logintype']
    chosen_log_in_input = form['username']
    password = form['password']




@app.route('/signup', methods=['GET', 'POST'])
def signup():
    clicked = False
    firstname = None
    if request.method == 'POST':
        clicked = True
        form = request.form
        firstname = get_signup_details(form)
        # print(form)
    return render_template('signup.html', clicked = clicked, firstname = firstname)

def get_signup_details(form):
    email = form['email']
    firstname = form['firstname']
    lastname = form['lastname']
    dob = form['dob']
    city = form['city']
    username = form['username']
    password = form['password']
    userid = 100
    add_a_new_user(userid, firstname, lastname, email, dob, city, username, password)
    return firstname

@app.route('/wordofday')
def wordofday():
    return render_template('wordofday.html')



if __name__ == '__main__':
    app.run(debug=True, port=5001)