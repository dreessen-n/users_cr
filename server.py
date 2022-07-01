from flask import Flask, render_template, render_template, request, redirect, session
from user import User

app = Flask(__name__)
app.secret_key='REinstall working well'

@app.route('/')
def index():
    """For this assignment redirect to users page"""
    return redirect('/users.html')

@app.route('/users')
def show_all():
    """Render All the users"""
    users = User.get_all()
    print(users)
    return render_template('users.html', all_users=users)

@app.route('/users/new', methods=['POST'])
def create_new_user():
    """Add a new user to db users"""
    #  First create a dict based on request form
    # The keys need to exactly match the variables in query string
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    # pass the data dict to the save_user() in User class
    User.save_user(data)
    # Do not forget to redirect after saving to db
    return redirect('/users')

@app.errorhandler(404)
def page_not_found(e):
    """Error handling for page not found"""
    return f'Sorry! No response. Try again.'

# Ensure file is run directly and not from different
# module, and run localhost on port 5001 for mac
if __name__=="__main__":
    app.run(host='localhost', port=5001, debug=True)
