from flask import Blueprint
from flask import Flask, render_template, url_for, request
from flask_login import login_required, logout_user
from werkzeug.utils import redirect
from Controller.send_email import *

home_route = Blueprint('home_route', __name__)


data = {
    "wishlist": ["Microsoft", "Google", "Uber"],
    "inprogress": ["Twitter", "Pearson"],
    "applied": ["Amazon", "NetApp"],
    "offers": ["Perfios"]
}

upcoming_events = [
    {"duedate": "28th Sept, 2021",
     "company": "Apple"
     },
    {"duedate": "19th Dec, 2021",
     "company": "Microsoft"
     },
    {"duedate": "21st Dec, 2021",
     "company": "Amazon"
     },
    {"duedate": "21st Dec, 2021",
     "company": "Amazon"
     },
    {"duedate": "21st Dec, 2021",
     "company": "Amazon"
     }
]

profile = {
    "name": "Jessica Holds",
    "Location": "Raleigh, NC",
    "phone_number": "",
    "social": {
            "linkedin": "www.linkedin.com/in/surajdm",

    }
}


@home_route.route('', methods=['GET'])
@login_required
def home():
    return render_template('home.html', data=data, upcoming_events=upcoming_events)


@home_route.route('/view', methods=['GET'])
@login_required
def view():
    card_selected = request.args.get('user')
    return render_template('view_list.html', data=data, upcoming_events=upcoming_events)

@home_route.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect("/login")

@home_route.route('/add_New',methods=['GET','POST'])
#@login_required
def add_New():
    #print(request.method)
    if request.method == "POST":
        company_name = request.form['fullname']
        location = request.form['location_text']
        Job_Profile = request.form['text']
        salary = request.form['sal']
        user = request.form['user']
        password = request.form['pass']
        email = request.form['user_email']
        sec_question = request.form['starting_date']
        sec_answer = request.form['starting_date']
        notes = request.form['notes']
        date_applied = request.form['starting_date']

    print("Adding New...")
    s_email(company_name,location, Job_Profile,salary, user,password,email,sec_question,sec_answer,notes,date_applied)
    print("Added Company to List")
    print("Email Notification Sent")
    return render_template('home.html', data=data, upcoming_events=upcoming_events)