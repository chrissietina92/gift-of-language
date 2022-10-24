from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')





@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form = request.form
        get_details(form)
        # print(form) #ImmutableMultiDict([('logintype', 'u'), ('username', 'hi'), ('password', 'Chrissie'), ('next', 'Next')])
    return render_template('login.html')

def get_details(form):
    chosen_log_in = form['logintype']
    chosen_log_in_input = form['username']
    password = form['password']




@app.route('/signup')
def signup():
    if request.method == 'POST':
        form = request.form
        get_details(form)
    return render_template('signup.html')




if __name__ == '__main__':
    app.run(debug=True, port=5001)