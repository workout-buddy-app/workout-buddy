from flask import Flask, flash, request, render_template, redirect, abort
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required

from config import SECRET_KEY

from database.users import add_user, email_available, get_user_with_credentials, get_user_by_id, get_public_profile_data, update_public_profile
from database.messages import get_messaged_users, get_messages_between_users, add_message
from database.match_ups import get_match
from database.quotes import get_random_quote

from api.smoothies import SmoothieManager

from utils.validation import is_over_eighteen


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


def render_template_with_quote(*args, **kwargs):
    quote = get_random_quote()
    return render_template(*args, **kwargs, quote=quote)


@app.get('/')
def view_home():
    return render_template_with_quote("home.html", user=current_user)


@app.get('/about')
def view_about():
    return render_template_with_quote('about.html', user=current_user)


@app.get('/workouts')
def view_workout():
    return render_template_with_quote('workouts.html', user=current_user)


@app.post('/workouts')
def search_workout():
    pass


@app.get('/smoothies')
def view_smoothies():
    ingredient = request.args.get('ingredient')
    if ingredient:
        smoothies_search_results = SmoothieManager.smoothie_search(ingredient)
        return smoothies_search_results
    else:
        smoothies_search_results = None
    return render_template('smoothies.html', user=current_user)


@app.get('/buddies')
@login_required
def find_a_buddy():
    if 'current_match' in request.args:
        match_requested = True
        matching_user = get_match(current_user.id, exclude=request.args.get('current_match'))
    else:
        match_requested = False
        matching_user = None
    return render_template_with_quote('buddies.html', user=current_user, match_requested=match_requested, matching_user=matching_user)


@app.get('/profile/<int:user_id>')
@login_required
def view_public_profile(user_id):
    user_data = get_public_profile_data(user_id)
    if not user_data:
        abort(404)
    return render_template_with_quote('publicprofile.html', user=current_user, user_data=user_data)


@app.get('/messages')
@login_required
def view_messages():
    other_users = get_messaged_users(current_user.id)
    return render_template_with_quote('messages.html', user=current_user, other_users=other_users, selected_user_id=None)


@app.get('/messages/<int:selected_user_id>')
@login_required
def view_messages_from(selected_user_id):
    other_users = get_messaged_users(current_user.id)
    messages = get_messages_between_users(current_user.id, selected_user_id)
    if not messages:
        abort(404)
    return render_template_with_quote('messages.html', user=current_user, other_users=other_users, selected_user_id=selected_user_id, messages=messages)


@app.post('/messages/<int:selected_user_id>')
@login_required
def send_message_to(selected_user_id):
    content = request.form.get('content')
    if content:
        add_message(current_user.id, selected_user_id, content)
    return redirect(f'/messages/{selected_user_id}')


@app.get('/profile')
@login_required
def view_own_profile():
    user_data = get_public_profile_data(current_user.id)
    return render_template_with_quote("profile.html", user=current_user, user_data=user_data)


@app.post('/profile')
@login_required
def edit_own_profile():
    display_name = request.form.get('display_name')
    about = request.form.get('about')
    location = request.form.get('location')
    update_public_profile(current_user.id, display_name, about, location)
    flash('Update successful!', 'info')
    return redirect('/profile')


@app.get('/login')
def view_login():
    if not current_user.is_anonymous:
        return redirect('/profile')
    return render_template_with_quote("login.html", user=current_user)


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
    return render_template_with_quote("signup.html", user=current_user)


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
    elif not is_over_eighteen(date_birth):
        flash("Users must be 18 or over", 'error')
    else:
        add_user(name, email, password, date_birth)
        flash("New account created.", 'info')
        return redirect('/login')
    return redirect('/signup')


@app.get('/logout')
@login_required
def submit_logout():
    logout_user()
    return redirect('/login')


@app.get('/disclaimer')
def disclaimer():
    return render_template_with_quote('disclaimer.html', user=current_user)


if __name__ == '__main__':
    app.run()
