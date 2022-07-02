from flask import Flask, render_template, render_template, request, redirect, session
from user import User

app = Flask(__name__)
app.secret_key='REinstall working well'

@app.route('/')
def index():
    """For this assignment redirect to users page"""
    return redirect('/users')

@app.route('/users')
def show_all():
    """Render All the users"""
    users = User.get_all()
    print(users)
    return render_template('users.html', all_users=users)

@app.route('/users/new')
def show_add_form():
    """Create form to add new user"""
    return render_template('new.html')

@app.route('/users/new/create', methods=["POST"] )
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

@app.route('/users/<int:user_id>')
def get_one(user_id):
    """Display one user"""
    user = User.get_user(user_id)
    print(user)
    return render_template('show_one.html', one_user=user)

@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    """Edit the user based on id"""
    user = User.get_user(user_id)
    return render_template('edit.html', one_user=user)

@app.route('/users/<int:user_id>/update', methods=['POST'])
def update_user(user_id):
    """Update the user info"""
    data = {
        'id': user_id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.update(data)
    print(id)
    return redirect('/users')

@app.route('/users/delete', methods=['POST'])
def delete_user():
    """Delete user based on id"""
    User.delete(request.form)
    return redirect('/')



@app.errorhandler(404)
def page_not_found(e):
    """Error handling for page not found"""
    return f'Sorry! No response. Try again.'

# Ensure file is run directly and not from different
# module, and run localhost on port 5001 for mac
if __name__=="__main__":
    app.run(host='localhost', port=5001, debug=True)
