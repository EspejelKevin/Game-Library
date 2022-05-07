from flask import Blueprint, redirect, render_template, request, url_for


start = Blueprint("start", __name__, template_folder="templates")


@start.route("/")
def index():
    return redirect(url_for("start.whois"))

@start.route("/whois", methods=["GET", "POST"])
def whois():
    if request.method == "POST":
        user = request.form.get("user")
        #print(user)
        if user == "employee":
            return redirect(url_for("auth.login_employee"))
        elif user == "customer":
            return redirect(url_for("auth.login_customer"))
    
    return render_template("start.html")
