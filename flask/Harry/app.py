from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

#Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Initialize the database
db = SQLAlchemy(app)

#Create the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80),nullable=False)
    last_name = db.Column(db.String(80),nullable=False)
    email = db.Column(db.String(80),nullable=False)
    password=db.Column(db.String(120),nullable=False)
    reEnter_password=db.Column(db.String(120),nullable=False)

#create the database and tables
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create-account', methods=['GET','POST'])
def register():
    #Get data from the form 
    if request.method == 'POST':
        first_name = request.form['fname']
        last_name =request.form['lname']
        email = request.form['email']
        password = request.form['psw']
        reEnter_password = request.form['psw-repeat']

        #check if user exists
        existing = User.query.filter_by(email=email)
        if existing:
            "User already exists"
        
        #create new user
        new_user = User(first_name=first_name,last_name=last_name,email=email,password=password,reEnter_password=reEnter_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form


@app.route('/users')
def display_users():
    users = User.query.all()

    return render_template('users.html')

if __name__ == '__main__':
    app.run(debug=True)