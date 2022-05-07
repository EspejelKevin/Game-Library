from flask import Blueprint, flash, redirect, render_template, request, url_for
from app.database.db_users import *
from app.database.db_employees import *
from werkzeug.security import check_password_hash, generate_password_hash


auth = Blueprint("auth", __name__, template_folder="templates", url_prefix="/auth", static_folder="static")


@auth.route("/login_employee", methods=["GET", "POST"])
def login_employee():
    return render_template("auth/login_employee.html")

@auth.route("/register_employee", methods=["GET", "POST"])
def register_employee():
    if request.method == "POST":
        no_employee = request.form.get("no_employee")
        name = request.form.get("name")
        lastname = request.form.get("lastname")
        email = request.form.get("email")
        password = request.form.get("pass")
        rol = request.form.get("rol")
        hashed_pass = generate_password_hash(password)

        if rol != "1" or rol != "2":
            rol = None
        else:
            rol = int(rol)

        data = (no_employee, name, lastname, email, hashed_pass, rol)

        if insert_employee(data):
            flash("Employee added successfully", "success")
            return redirect(url_for("auth.login_employee"))
        else:
            flash("Error adding employee", "error")

    return render_template("auth/register_employee.html")

@auth.route("/login_customer", methods=["GET", "POST"])
def login_customer():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["pass"]
        user = get_user_by_username(username)

        if user is not None:
            if check_password_hash(user[3], password):
                flash("You are logged in", "success")
                return render_template("auth/login_customer.html")
            else:
                flash("Invalid password", "error")
        else:
            flash("User does not exist", "error")

    return render_template("auth/login_customer.html")

@auth.route("/register_customer", methods=["GET", "POST"])
def register_customer():
    if request.method == "POST":
        username = request.form["_username"]
        name = request.form["_name"]
        lastname = request.form["_lastname"]
        email = request.form["_email"]
        password = request.form["_pass"]
        hashed_pass = generate_password_hash(password)
        age = request.form["_age"]

        data = (username, email, hashed_pass, name, lastname, age)
        if insert_user(data):
            flash("Customer created successfully", "success")
            return redirect(url_for("auth.login_customer"))
        else:
            flash("Customer creation failed", "error")
            
    return render_template("auth/register_customer.html")



