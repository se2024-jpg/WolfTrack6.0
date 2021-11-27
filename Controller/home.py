from flask import Blueprint
from flask import Flask, render_template, url_for, request
from flask_login import login_required, logout_user, current_user
from werkzeug.utils import redirect,send_from_directory
from Controller.send_email import *
from Controller.send_profile import *
from Controller.ResumeParser import *
import os
from flask import send_file, current_app as app
from Controller.data import data, upcoming_events, profile

home_route = Blueprint('home_route', __name__)


@home_route.route('', methods=['GET'])
def home():
    if current_user.is_authenticated:
        return render_template('home.html', data=data, upcoming_events=upcoming_events)
    else:
        return render_template('main_login.html')


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

@home_route.route('/send_Profile',methods=['GET','POST'])
def send_Profile():
    emailID = request.form['emailID']
    print("Mailing Profile...")
    s_profile(data,upcoming_events, profile,emailID)
    print("Email Notification Sent")
    return render_template('home.html', data=data, upcoming_events=upcoming_events)


filename=""
@home_route.route("/upload", methods=['POST'])
def upload():
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    target = os.path.join(APP_ROOT, 'resume/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    #print(target + os.listdir(target)[0])
    if len(os.listdir(target)) != 0:
        os.remove(target + os.listdir(target)[0])

    for file in request.files.getlist("file"):
        filename = file.filename
        destination = "/".join([target, filename])
        file.save(destination)

    return render_template("home.html", data=data, upcoming_events=upcoming_events)

@home_route.route('/resumeAnalyzer', methods=['GET'])
@login_required
def view_ResumeAna():
    return render_template('resume_analyzer.html')

@home_route.route('/analyze_resume', methods=['POST'])
@login_required
def analyze_resume():
    jobtext = request.form['jobtext']
    print(jobtext)
    os.chdir(os.getcwd()+"/Controller/resume/")
    output = resume_analyzer(jobtext, str(os.listdir(os.getcwd())[0]))
    os.chdir("..")
    os.chdir("..")
    print(output)
    return render_template('resume_analyzer.html', data = output)

@home_route.route("/display/", methods=['POST'])
def display():
    path = os.getcwd()+"/Controller/resume/"
    filename = os.listdir(path)
    return send_file(path+str(filename[0]), attachment_filename= str(filename[0]))
