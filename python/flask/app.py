"""
Flask Application: Управление Университетами и Студентами

Архитектура:
- Models: User, University, Student (SQLAlchemy ORM)
- Routes: @app.route() маршруты с обработчиками
- Templates: Jinja2 шаблоны с наследованием
- Auth: Flask-Login для аутентификации

Поток запроса:
1. HTTP-запрос на маршрут (GET /universities)
2. @app.route() находит соответствующую функцию
3. Функция выполняет логику (получает данные из БД)
4. render_template() подставляет данные в шаблон
5. Шаблон рендерится в HTML
6. Возвращается HTTP-ответ
"""

# ========================================
# ИМПОРТЫ
# ========================================
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from datetime import datetime, date

# ========================================
# ИНИЦИАЛИЗАЦИЯ FLASK
# ========================================

app = Flask(__name__)

# Секретный ключ для сессий (ДОЛЖЕН БЫТЬ СЛУЧАЙНЫМ В PRODUCTION!)
app.config['SECRET_KEY'] = 'your_secret_key_12345'

# Конфигурация БД
# Текущий вариант: MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://django_user:django_password@127.0.0.1:3306/django_db'

# Отключить предупреждения о изменении отслеживания
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Инициализация БД (ORM)
db = SQLAlchemy(app)

# Инициализация системы логинизации
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Куда редирект если не авторизован
login_manager.login_message = 'Пожалуйста, войдите для доступа к этой странице.'

# ========================================
# МОДЕЛИ (ORM - Object-Relational Mapping)
# ========================================

class User(UserMixin, db.Model):
    """
    UserMixin добавляет методы:
    - is_authenticated: True если пользователь вошел
    - is_active: True если аккаунт активен
    - is_anonymous: True если это анонимный пользователь
    - get_id(): возвращает ID пользователя
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)


class University(db.Model):
    """
    Модель университета.
    
    Поля:
    - id: первичный ключ (автоинкремент)
    - full_name: полное название
    - short_name: сокращенное название
    - established_date: дата основания
    - students: связь с таблицей Student (один-ко-многим)
    """
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    short_name = db.Column(db.String(50), nullable=False)
    established_date = db.Column(db.Date, nullable=False)
    
    # Связь с Student (один университет - много студентов)
    # backref='university' - добавляет обратную ссылку в Student
    students = db.relationship('Student', backref='university', lazy=True)
    
    def __repr__(self):
        return f'<University {self.short_name}>'


class Student(db.Model):
    """
    Модель студента.
    
    Поля:
    - id: первичный ключ
    - full_name: ФИО студента
    - birth_date: дата рождения
    - university_id: внешний ключ (ID университета)
    - enrollment_year: год поступления
    """
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    
    # INT - ID университета (внешний ключ)
    university_id = db.Column(db.Integer, db.ForeignKey('university.id'), nullable=False)
    
    enrollment_year = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'<Student {self.full_name}>'


# ========================================
# СИСТЕМА АУТЕНТИФИКАЦИИ
# ========================================

@login_manager.user_loader
def load_user(user_id):
    """
    Загружает пользователя по ID.
    Вызывается автоматически при каждом запросе.
    """
    return User.query.get(int(user_id))


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Форма входа.
    
    GET: показывает форму
    POST: проверяет логин/пароль и создает сессию
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Ищем пользователя в БД
        user = User.query.filter_by(username=username).first()
        
        # Простая проверка пароля (в боевом коде нужно хешировать!)
        if user and user.password == password:
            # Создаем сессию
            login_user(user)
            
            # Редирект на следующую страницу или на главную
            next_page = request.args.get('next')
            return redirect(next_page or url_for('universities'))
        
        flash('Неверное имя пользователя или пароль', 'danger')
    
    return render_template('login.html')


@app.route('/logout')
@login_required  # Только авторизованные
def logout():
    """Выход из системы"""
    logout_user()
    flash('Вы успешно вышли из системы', 'success')
    return redirect(url_for('login'))


# ========================================
# МАРШРУТЫ - УНИВЕРСИТЕТЫ
# ========================================

@app.route('/')
def index():
    """Главная страница - редирект на университеты"""
    return redirect(url_for('universities'))


@app.route('/universities')
def universities():
    """
    Список всех университетов (ПУБЛИЧНЫЙ, без логина).
    
    Поддерживает:
    - /universities - все университеты
    - /universities?q=МГУ - поиск по названию
    - /universities?page=2 - пагинация
    """
    query = request.args.get('q', '')
    page = request.args.get('page', 1, type=int)
    per_page = 10
    
    if query:
        # Ищем в полном названии ИЛИ сокращенном
        universities_list = University.query.filter(
            (University.full_name.contains(query)) | 
            (University.short_name.contains(query))
        ).order_by(University.full_name).paginate(page=page, per_page=per_page)
    else:
        # Все университеты
        universities_list = University.query.order_by(
            University.full_name
        ).paginate(page=page, per_page=per_page)
    
    return render_template('universities.html', 
                         universities=universities_list, 
                         query=query)


@app.route('/universities/create', methods=['GET', 'POST'])
@login_required  # ← ЗАЩИТА: только авторизованные
def create_university():
    """
    Создание нового университета.
    
    GET: показывает форму
    POST: сохраняет в БД
    """
    if request.method == 'POST':
        full_name = request.form['full_name']
        short_name = request.form['short_name']
        established_date = request.form['established_date']
        
        # Проверка уникальности сокращения
        if University.query.filter_by(short_name=short_name).first():
            flash('Университет с таким сокращением уже существует', 'danger')
            return render_template('university_form.html')
        
        # Создаем новый объект
        university = University(
            full_name=full_name, 
            short_name=short_name, 
            established_date=datetime.strptime(established_date, '%Y-%m-%d').date()
        )
        
        # Добавляем в сессию и коммитим (сохраняем в БД)
        db.session.add(university)
        db.session.commit()
        
        flash('Университет успешно создан', 'success')
        return redirect(url_for('universities'))
    
    return render_template('university_form.html')


@app.route('/universities/<int:id>/update', methods=['GET', 'POST'])
@login_required  # ← ЗАЩИТА
def update_university(id):
    """Редактирование университета"""
    
    # Получаем университет или 404
    university = University.query.get_or_404(id)
    
    if request.method == 'POST':
        university.full_name = request.form['full_name']
        university.short_name = request.form['short_name']
        university.established_date = datetime.strptime(
            request.form['established_date'], '%Y-%m-%d'
        ).date()
        
        db.session.commit()
        flash('Университет успешно обновлен', 'success')
        return redirect(url_for('universities'))
    
    return render_template('university_form.html', university=university)


@app.route('/universities/<int:id>/delete', methods=['POST'])
@login_required  # ← ЗАЩИТА
def delete_university(id):
    """Удаление университета"""
    
    university = University.query.get_or_404(id)
    
    # Проверка: нельзя удалить, если есть студенты
    if university.students:
        flash('Нельзя удалить университет, в котором есть студенты', 'danger')
        return redirect(url_for('universities'))
    
    db.session.delete(university)
    db.session.commit()
    flash('Университет успешно удален', 'success')
    return redirect(url_for('universities'))


# ========================================
# МАРШРУТЫ - СТУДЕНТЫ
# ========================================

@app.route('/students')
def students():
    """
    Список всех студентов (ПУБЛИЧНЫЙ).
    
    Поддерживает:
    - /students - все студенты
    - /students?q=Иван - поиск по ФИО
    - /students?university_id=1 - фильтр по университету
    - /students?page=2 - пагинация
    """
    query = request.args.get('q', '')
    university_id = request.args.get('university_id', type=int)
    page = request.args.get('page', 1, type=int)
    per_page = 10
    
    # Начинаем с базового запроса
    students_query = Student.query
    
    # Добавляем условия если есть
    if query:
        students_query = students_query.filter(Student.full_name.contains(query))
    
    if university_id:
        students_query = students_query.filter(Student.university_id == university_id)
    
    # Пагинируем и сортируем
    students_list = students_query.order_by(
        Student.full_name
    ).paginate(page=page, per_page=per_page)
    
    # Получаем все университеты для фильтра в шаблоне
    universities = University.query.all()
    
    return render_template('students.html', 
                         students=students_list, 
                         universities=universities,
                         query=query, 
                         selected_university=university_id)


@app.route('/students/create', methods=['GET', 'POST'])
@login_required  # ← ЗАЩИТА
def create_student():
    """Создание нового студента"""
    
    universities = University.query.all()
    
    if request.method == 'POST':
        full_name = request.form['full_name']
        birth_date = request.form['birth_date']
        university_id = request.form['university_id']
        enrollment_year = request.form['enrollment_year']
        
        # Валидация года
        current_year = datetime.now().year
        if int(enrollment_year) < 1900 or int(enrollment_year) > current_year + 1:
            flash('Некорректный год поступления', 'danger')
            return render_template('student_form.html', universities=universities)
        
        # Создаем студента
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
@login_required  # ← ЗАЩИТА
def update_student(id):
    """Редактирование студента"""
    
    student = Student.query.get_or_404(id)
    universities = University.query.all()
    
    if request.method == 'POST':
        student.full_name = request.form['full_name']
        student.birth_date = datetime.strptime(
            request.form['birth_date'], '%Y-%m-%d'
        ).date()
        student.university_id = request.form['university_id']
        student.enrollment_year = request.form['enrollment_year']
        
        db.session.commit()
        flash('Студент успешно обновлен', 'success')
        return redirect(url_for('students'))
    
    return render_template('student_form.html', student=student, universities=universities)


@app.route('/students/<int:id>/delete', methods=['POST'])
@login_required  # ← ЗАЩИТА
def delete_student(id):
    """Удаление студента"""
    
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    flash('Студент успешно удален', 'success')
    return redirect(url_for('students'))


# ========================================
# КОНТЕКСТНЫЕ ПРОЦЕССОРЫ (помощники в шаблонах)




























    app.run(debug=True, host='0.0.0.0', port=5000)    # debug=True: перезагружает сервер при изменении кода    # Запускает сервер            db.create_all()    with app.app_context():    # Создает все таблицы, если их еще нетif __name__ == '__main__':# ========================================# ЗАПУСК ПРИЛОЖЕНИЯ# ========================================    return dict(format_date=format_date, now=datetime.now())            return date_obj.strftime('%d.%m.%Y') if date_obj else ''        """Форматирует дату как ДД.МММ.ГГГГ"""    def format_date(date_obj):    """    Теперь в любом шаблоне можно использовать format_date()    Добавляет полезные функции в шаблоны.    """def utility_processor():@app.context_processor# ========================================    # Запускаем сервер разработки
    app.run(debug=True, host='0.0.0.0', port=5000)