from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://django_user:django_password@127.0.0.1:3306/django_db'
app.config['SECRET_KEY'] = 'your_secret_key_12345'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Пожалуйста, войдите для доступа к этой странице.'

# ------------------------
# MODELS
# ------------------------
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

class University(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    short_name = db.Column(db.String(50), nullable=False)
    established_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'<University {self.short_name}>'

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    university_id = db.Column(db.Integer, db.ForeignKey('university.id'), nullable=False)
    enrollment_year = db.Column(db.Integer, nullable=False)
    university = db.relationship('University', backref=db.backref('students', lazy=True))

    def __repr__(self):
        return f'<Student {self.full_name}>'

# ------------------------
# LOGIN MANAGER
# ------------------------
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ------------------------
# ROUTES
# ------------------------
@app.route('/')
def index():
    return redirect(url_for('universities'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        # Простая проверка пароля (без хеширования для простоты)
        if user and user.password == password:
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('universities'))
        flash('Неверное имя пользователя или пароль', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Вы успешно вышли из системы', 'success')
    return redirect(url_for('login'))

# ----- Universities -----
@app.route('/universities')
def universities():
    query = request.args.get('q', '')
    page = request.args.get('page', 1, type=int)
    per_page = 10
    
    if query:
        universities_list = University.query.filter(
            University.full_name.contains(query) | 
            University.short_name.contains(query)
        ).order_by(University.full_name).paginate(page=page, per_page=per_page)
    else:
        universities_list = University.query.order_by(University.full_name).paginate(page=page, per_page=per_page)
    
    return render_template('universities.html', 
                         universities=universities_list, 
                         query=query)

@app.route('/universities/create', methods=['GET', 'POST'])
@login_required
def create_university():
    if request.method == 'POST':
        full_name = request.form['full_name']
        short_name = request.form['short_name']
        established_date = request.form['established_date']
        
        # Проверка на уникальность
        if University.query.filter_by(short_name=short_name).first():
            flash('Университет с таким сокращенным названием уже существует', 'danger')
            return render_template('university_form.html')
        
        university = University(
            full_name=full_name, 
            short_name=short_name, 
            established_date=datetime.strptime(established_date, '%Y-%m-%d').date()
        )
        db.session.add(university)
        db.session.commit()
        flash('Университет успешно создан', 'success')
        return redirect(url_for('universities'))
    
    return render_template('university_form.html')

@app.route('/universities/<int:id>/update', methods=['GET', 'POST'])
@login_required
def update_university(id):
    university = University.query.get_or_404(id)
    
    if request.method == 'POST':
        university.full_name = request.form['full_name']
        university.short_name = request.form['short_name']
        university.established_date = datetime.strptime(request.form['established_date'], '%Y-%m-%d').date()
        
        db.session.commit()
        flash('Университет успешно обновлен', 'success')
        return redirect(url_for('universities'))
    
    return render_template('university_form.html', university=university)

@app.route('/universities/<int:id>/delete', methods=['POST'])
@login_required
def delete_university(id):
    university = University.query.get_or_404(id)
    
    # Проверяем, есть ли студенты в этом университете
    if university.students:
        flash('Нельзя удалить университет, в котором есть студенты', 'danger')
        return redirect(url_for('universities'))
    
    db.session.delete(university)
    db.session.commit()
    flash('Университет успешно удален', 'success')
    return redirect(url_for('universities'))

# ----- Students -----
@app.route('/students')
def students():
    query = request.args.get('q', '')
    university_id = request.args.get('university_id', type=int)
    page = request.args.get('page', 1, type=int)
    per_page = 10
    
    students_query = Student.query
    
    if query:
        students_query = students_query.filter(Student.full_name.contains(query))
    
    if university_id:
        students_query = students_query.filter(Student.university_id == university_id)
    
    students_list = students_query.order_by(Student.full_name).paginate(page=page, per_page=per_page)
    universities = University.query.all()
    
    return render_template('students.html', 
                         students=students_list, 
                         universities=universities,
                         query=query, 
                         selected_university=university_id)

@app.route('/students/create', methods=['GET', 'POST'])
@login_required
def create_student():
    universities = University.query.all()
    
    if request.method == 'POST':
        full_name = request.form['full_name']
        birth_date = request.form['birth_date']
        university_id = request.form['university_id']
        enrollment_year = request.form['enrollment_year']
        
        # Проверка года поступления
        current_year = datetime.now().year
        if int(enrollment_year) < 1900 or int(enrollment_year) > current_year + 1:
            flash('Некорректный год поступления', 'danger')
            return render_template('student_form.html', universities=universities)
        
        student = Student(
            full_name=full_name,
            birth_date=datetime.strptime(birth_date, '%Y-%m-%d').date(),
            university_id=university_id,
            enrollment_year=enrollment_year
        )
        db.session.add(student)
        db.session.commit()
        flash('Студент успешно создан', 'success')
        return redirect(url_for('students'))
    
    return render_template('student_form.html', universities=universities)

@app.route('/students/<int:id>/update', methods=['GET', 'POST'])
@login_required
def update_student(id):
    student = Student.query.get_or_404(id)
    universities = University.query.all()
    
    if request.method == 'POST':
        student.full_name = request.form['full_name']
        student.birth_date = datetime.strptime(request.form['birth_date'], '%Y-%m-%d').date()
        student.university_id = request.form['university_id']
        student.enrollment_year = request.form['enrollment_year']
        
        db.session.commit()
        flash('Студент успешно обновлен', 'success')
        return redirect(url_for('students'))
    
    return render_template('student_form.html', student=student, universities=universities)

@app.route('/students/<int:id>/delete', methods=['POST'])
@login_required
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    flash('Студент успешно удален', 'success')
    return redirect(url_for('students'))

@app.context_processor
def utility_processor():
    def format_date(date):
        return date.strftime('%d.%m.%Y') if date else ''
    return dict(format_date=format_date)

if __name__ == '__main__':
    app.run(debug=True)