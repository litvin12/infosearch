from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://django_user:django_password@127.0.0.1:3306/django_db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

class University(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    short_name = db.Column(db.String(50), nullable=False)
    established_date = db.Column(db.Date, nullable=False)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    university_id = db.Column(db.Integer, db.ForeignKey('university.id'), nullable=False)
    enrollment_year = db.Column(db.Integer, nullable=False)
    university = db.relationship('University', backref=db.backref('students', lazy=True))

# Login manager
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    return redirect(url_for('universities'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('universities'))
        flash('Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/universities')
def universities():
    query = request.args.get('q', '')
    universities = University.query.filter(University.full_name.contains(query)).all()
    return render_template('universities.html', universities=universities, query=query)

@app.route('/universities/create', methods=['GET', 'POST'])
@login_required
def create_university():
    if request.method == 'POST':
        full_name = request.form['full_name']
        short_name = request.form['short_name']
        established_date = request.form['established_date']
        university = University(full_name=full_name, short_name=short_name, established_date=established_date)
        db.session.add(university)
        db.session.commit()
        return redirect(url_for('universities'))
    return render_template('university_form.html')

@app.route('/universities/<int:id>/update', methods=['GET', 'POST'])
@login_required
def update_university(id):
    university = University.query.get_or_404(id)
    if request.method == 'POST':
        university.full_name = request.form['full_name']
        university.short_name = request.form['short_name']
        university.established_date = request.form['established_date']
        db.session.commit()
        return redirect(url_for('universities'))
    return render_template('university_form.html', university=university)

@app.route('/universities/<int:id>/delete', methods=['POST'])
@login_required
def delete_university(id):
    university = University.query.get_or_404(id)
    db.session.delete(university)
    db.session.commit()
    return redirect(url_for('universities'))

@app.route('/students')
def students():
    query = request.args.get('q', '')
    students = Student.query.filter(Student.full_name.contains(query)).all()
    return render_template('students.html', students=students, query=query)

@app.route('/students/create', methods=['GET', 'POST'])
@login_required
def create_student():
    universities = University.query.all()
    if request.method == 'POST':
        full_name = request.form['full_name']
        birth_date = request.form['birth_date']
        university_id = request.form['university_id']
        enrollment_year = request.form['enrollment_year']
        student = Student(full_name=full_name, birth_date=birth_date, university_id=university_id, enrollment_year=enrollment_year)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('students'))
    return render_template('student_form.html', universities=universities)

@app.route('/students/<int:id>/update', methods=['GET', 'POST'])
@login_required
def update_student(id):
    student = Student.query.get_or_404(id)
    universities = University.query.all()
    if request.method == 'POST':
        student.full_name = request.form['full_name']
        student.birth_date = request.form['birth_date']
        student.university_id = request.form['university_id']
        student.enrollment_year = request.form['enrollment_year']
        db.session.commit()
        return redirect(url_for('students'))
    return render_template('student_form.html', student=student, universities=universities)

@app.route('/students/<int:id>/delete', methods=['POST'])
@login_required
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('students'))

if __name__ == '__main__':
    app.run(debug=True)
