from flask import Flask, jsonify, request, render_template
from db_functions import add_a_new_user, username_and_password_match
from daily_words import randomWordGenerator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    clicked = False
    log_in_right = False
    if request.method == 'POST':
        clicked = True
        form = request.form
        log_in_right = get_login_details(form)
        # print(form) # returns ImmutableMultiDict([('logintype', 'u'), ('username', 'hi'), ('password', 'Chrissie'), ('next', 'Next')])
    return render_template('login.html', clicked = clicked, log_in_right = log_in_right)

def get_login_details(form):
    column = form['logintype']
    print(column)
    value = form['username']
    password = form['password']
    log_in_right = username_and_password_match(column, value, password)
    return log_in_right




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
    word_of_day = randomWordGenerator()
    word = word_of_day[0]
    definition = word_of_day[1]
    return render_template('wordofday.html', word = word, definition = definition)


@app.route('/searchword', methods=['GET', 'POST'])
def searchword():
    clicked = False
    word_searched = ''
    if request.method == 'POST':
        clicked = True
        form = request.form
        word_searched = form['searchword']
        #add in the search word function
    return render_template('searchword.html', clicked = clicked, word_searched = word_searched)



if __name__ == '__main__':
    app.run(debug=True, port=5001)