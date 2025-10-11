from app import app, db, User

def init_db():
    with app.app_context():
        db.create_all()

        # Создаем пользователя admin с простым паролем
        if not User.query.filter_by(username='admin').first():
            admin = User(username='admin', password='1234')
            db.session.add(admin)
            db.session.commit()
            print("✅ Admin user created: login='admin', password='1234'")
        else:
            print("ℹ️ Admin user already exists.")

if __name__ == '__main__':
    init_db()
