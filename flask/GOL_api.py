from flask import Flask, request, render_template
from src.db_functions import add_a_new_user, username_and_password_match, get_user_by_id, get_user_by_column
from src.daily_words import randomWordGenerator
from src.dictionaryapi_functions import show_word_and_definition
from src.db_searched_words import add_searched_word


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    clicked = False
    log_in_right = False
    userid = 0
    if request.method == 'POST':
        clicked = True
        form = request.form
        print(form)
        login_details = get_login_details(form)
        log_in_right = login_details[0]
        column = login_details[1]
        value = login_details[2]
        userid = get_user_by_column(column, value)
        # print(form) # returns ImmutableMultiDict([('logintype', 'u'), ('username', 'hi'), ('password', 'Chrissie'), ('next', 'Next')])
    return render_template('login.html', userid = userid, clicked=clicked, log_in_right=log_in_right)


def get_login_details(form):
    column = form['logintype']
    print(column)
    value = form['username']
    password = form['password']
    log_in_right = username_and_password_match(column, value, password)
    return log_in_right, column, value


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    clicked = False
    firstname = None
    userid = 0
    if request.method == 'POST':
        clicked = True
        form = request.form
        signupdetails = get_signup_details(form)
        firstname = signupdetails[0]
        email = signupdetails[1]
        userid = get_user_by_column('Email', email)
        # print(form)
    return render_template('signup.html', clicked=clicked, userid = userid,  firstname=firstname)


def get_signup_details(form):
    email = form['email']
    firstname = form['firstname']
    lastname = form['lastname']
    dob = form['dob']
    city = form['city']
    username = form['username']
    password = form['password']

    add_a_new_user(firstname, lastname, email, dob, city, username, password)
    return firstname, email


# @app.route('/wordofday', methods=['GET', 'POST'])
# def wordofday():
#     clicked = False
#     word = ''
#     definition = ''
#     if request.method == 'POST':
#         clicked = True
#         word_of_day = randomWordGenerator()
#         word = word_of_day[0]
#         definition = word_of_day[1]
#     return render_template('wordofday.html', word = word, definition = definition , clicked=clicked)



# @app.route('/searchword', methods=['GET', 'POST'])
# def searchword():
#     clicked = False
#     word_searched = ''
#     if request.method == 'POST':
#         clicked = True
#         form = request.form
#         print(form)
#         the_word = form['searchword']
#         word_searched = show_word_and_definition(the_word)
#         add_searched_word(the_word)
#         # add in the search word function
#     return render_template('searchword.html', clicked=clicked, word_searched=word_searched)


@app.route('/searchword/<int:userid>', methods=['GET', 'POST'])
def searchword_by_id(userid):
    users = get_user_by_id(userid)
    userid = users[0][0]
    firstname = users[0][1]
    clicked = False
    word_searched = ''
    if request.method == 'POST':
        clicked = True
        form = request.form
        # print(form)
        the_word = form['searchword']
        word_searched = show_word_and_definition(the_word)
        add_searched_word(the_word) #add userid after
        # add in the search word function
    return render_template('searchword.html', firstname = firstname, userid = userid, clicked=clicked, word_searched=word_searched)

@app.route('/wordofday/<int:userid>', methods=['GET', 'POST'])
def wordofday_by_id(userid):
    users = get_user_by_id(userid)
    userid = users[0][0]
    # defaults = {'userid': userid}
    clicked = False
    word = ''
    definition = ''
    firstname = users[0][1]
    if request.method == 'POST':
        clicked = True
        word_of_day = randomWordGenerator()
        word = word_of_day[0]
        definition = word_of_day[1]
    return render_template('wordofday.html', firstname = firstname, userid = userid, word = word, definition = definition , clicked=clicked)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
