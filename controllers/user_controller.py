from flask import Blueprint, request, render_template, redirect, url_for, flash
from models.user_model import insert_user, get_users

user_bp = Blueprint('user_bp', __name__)

# Display the list of users
@user_bp.route('/users', methods=['GET'])
def get_all_users():
    users = get_users()
    return render_template('user_list.html', users=users)

# Display the form to add a new user
@user_bp.route('/users/add', methods=['GET'])
def add_user_form():
    return render_template('add_user.html')

# Handle the form submission to add a new user
@user_bp.route('/users/add', methods=['POST'])
def add_user():
    username = request.form.get('username')
    email = request.form.get('email')

    if username and email:
        insert_user(username, email)
        flash("User added successfully!", 'success')
        return redirect(url_for('user_bp.get_all_users'))
    else:
        flash("Please provide both username and email!", 'danger')
        return redirect(url_for('user_bp.add_user_form'))
