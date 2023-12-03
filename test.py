import os
from flask import Flask,render_template,request,redirect,url_for,send_from_directory
from werkzeug.utils import secure_filename


app = Flask(__name__, static_url_path='/static', static_folder='static')

ALLOWED_EXTENSIONS = set(['csv'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route("/")
def start():
    return render_template('login.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/result",methods = ["POST","GET"])
def result():
    UserName = ["saviru","mendis"]
    PassWord = ["123","123"]
    userNotFound = True
    username = request.form.get("username")
    password = request.form.get("password")
    message = ""


    for name in UserName:
        if username == name:
            userNotFound = False
            if password in PassWord:
                return render_template("home.html")
            else:
                message = "wrong password"                    
                return render_template("login.html",message = message)
            break

            
    if userNotFound:
        message  = "We cannot find your username "
        return render_template("login.html",message = message)
    
    return render_template("home.html",message = message)



@app.route("/about")
def about():
    return render_template("about.html")
    
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/upload1")
def upload1():
    return render_template("upload.html")

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            new_filename = f'{filename.split(".")[0]}_uplodedFile.csv'
            file.save(os.path.join('input', new_filename))
        return "uploded"
    return render_template('upload.html')



if __name__ == "__name__":
    app.run(debug=True)































#set FLASK_APP=test.py
#set FLASK_DEBUG=1
#flask run