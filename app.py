from flask import Flask, flash, request, render_template, redirect
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required

from config import SECRET_KEY

from database.users import add_user, add_user_to_data_table, email_available, get_user_with_credentials, get_user_by_id, update_public_profile

app = Flask(__name__)
app.secret_key = SECRET_KEY

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/login'
login_manager.login_message = 'Please log in to view this page.'
login_manager.login_message_category = 'error'


class User(UserMixin):

    def __init__(self, user_details):
        self.id = user_details.get('user_id')  # This one is important - it needs to be called self.id
        self.name = user_details.get('name')
        self.email = user_details.get('email')


@login_manager.user_loader
def user_loader(user_id):
    user_details = get_user_by_id(user_id)
    if user_details is None:
        return None
    user = User(user_details)
    return user


@app.get('/login')
def view_login():
    if not current_user.is_anonymous:
        return redirect('/profile')
    return render_template("login.html")


@app.post('/login')
def submit_login():
    if not current_user.is_anonymous:
        return redirect('/profile')
    email = request.form.get('email')
    password = request.form.get('password')
    user = get_user_with_credentials(email, password)
    if user is None:
        flash("Invalid credentials.", 'error')
    else:
        user = User(user)
        login_user(user)
        return redirect('/profile')
    return redirect('/login')


@app.get('/signup')
def view_signup():
    if not current_user.is_anonymous:
        return redirect('/profile')
    return render_template("signup.html")


@app.post('/signup')
def submit_signup():
    if not current_user.is_anonymous:
        return redirect('/profile')
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    date_birth = request.form.get('date_birth')
    if len(password) < 8:
        flash("Passwords should be at least 8 characters long.", 'error')
    elif not email_available(email):
        flash("An account with that email already exists.", 'error')
    else:
        add_user(name, email, password, date_birth)
        flash("New account created.", 'info')
        return redirect('/login')
    return redirect('/signup')


@app.post('/logout')
@login_required
def submit_logout():
    logout_user()
    return redirect('/login')


@app.get('/profile')
@login_required
def view_own_profile():
    return render_template("profile.html", user=current_user)


@app.get('/update')
@login_required
def view_update():
    return render_template('/update.html', user=current_user)


@app.post('/update')
@login_required
def update_profile():
    user = current_user.id
    display_name = request.form.get('display_name')
    about = request.form.get('about')
    location = request.form.get('location')
    update_public_profile(display_name, about, location, user)
    flash("Success!")
    return redirect('/profile')


#view pages:
@app.get('/')
def view_home():
    return render_template("home.html")


@app.get('/workouts')
def workout():
    return render_template('/workouts.html')


@app.get('/about')
def about():
    return render_template('/about.html')


@app.get('/disc')
def disc():
    return render_template('/disc.html')


@app.get('/publicprofile')
def other_user_profile():
    return render_template('/publicprofile.html')


@app.get('/findabuddy')
def find_a_buddy():
    return render_template('/findabuddy.html')


if __name__ == '__main__':
    app.run()
