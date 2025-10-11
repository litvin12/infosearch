from app import db, User
from werkzeug.security import generate_password_hash

def init_db():
    # Создаем таблицы в базе данных
    db.create_all()

    # Создаем пользователя-администратора
    if not User.query.filter_by(username='admin').first():
        admin = User(username='admin', password=generate_password_hash('password'))
        db.session.add(admin)
        db.session.commit()
        print("Admin user created with username: 'admin' and password: 'password'")
    else:
        print("Admin user already exists.")

if __name__ == '__main__':
    init_db()
