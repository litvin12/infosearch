from app import app, db, User, University, Student
from datetime import date

def init_db():
    with app.app_context():
        db.create_all()

        # Создаем пользователя admin
        if not User.query.filter_by(username='admin').first():
            admin = User(username='admin', password='1234')
            db.session.add(admin)
            print("✅ Admin user created: login='admin', password='1234'")
        else:
            print("ℹ️ Admin user already exists.")

        # Создаем тестовые университеты
        universities_data = [
            {
                'full_name': 'Московский государственный университет имени М.В. Ломоносова',
                'short_name': 'МГУ',
                'established_date': date(1755, 1, 25)
            },
            {
                'full_name': 'Санкт-Петербургский государственный университет',
                'short_name': 'СПбГУ', 
                'established_date': date(1724, 1, 28)
            },
            {
                'full_name': 'Новосибирский национальный исследовательский государственный университет',
                'short_name': 'НГУ',
                'established_date': date(1959, 1, 9)
            },
            {
                'full_name': 'Московский физико-технический институт',
                'short_name': 'МФТИ',
                'established_date': date(1946, 9, 25)
            },
            {
                'full_name': 'Национальный исследовательский университет "Высшая школа экономики"',
                'short_name': 'ВШЭ',
                'established_date': date(1992, 11, 27)
            }
        ]

        universities_created = 0
        for uni_data in universities_data:
            if not University.query.filter_by(short_name=uni_data['short_name']).first():
                university = University(**uni_data)
                db.session.add(university)
                universities_created += 1

        if universities_created > 0:
            print(f"✅ Created {universities_created} universities")
        else:
            print("ℹ️ Universities already exist")

        # Фиксируем университеты для создания студентов
        db.session.commit()

        # Создаем тестовых студентов
        students_data = [
            {
                'full_name': 'Иванов Алексей Сергеевич',
                'birth_date': date(2000, 5, 15),
                'university_id': 1,  # МГУ
                'enrollment_year': 2018
            },
            {
                'full_name': 'Петрова Мария Владимировна', 
                'birth_date': date(2001, 8, 22),
                'university_id': 1,  # МГУ
                'enrollment_year': 2019
            },
            {
                'full_name': 'Сидоров Дмитрий Иванович',
                'birth_date': date(1999, 12, 3),
                'university_id': 2,  # СПбГУ
                'enrollment_year': 2017
            },
            {
                'full_name': 'Козлова Анна Петровна',
                'birth_date': date(2002, 3, 30),
                'university_id': 2,  # СПбГУ  
                'enrollment_year': 2020
            },
            {
                'full_name': 'Федоров Сергей Николаевич',
                'birth_date': date(2000, 7, 18),
                'university_id': 3,  # НГУ
                'enrollment_year': 2018
            },
            {
                'full_name': 'Никитина Елена Александровна',
                'birth_date': date(2001, 1, 10),
                'university_id': 3,  # НГУ
                'enrollment_year': 2019
            },
            {
                'full_name': 'Васильев Павел Олегович',
                'birth_date': date(1999, 9, 5),
                'university_id': 4,  # МФТИ
                'enrollment_year': 2017
            },
            {
                'full_name': 'Морозова Ольга Дмитриевна',
                'birth_date': date(2002, 11, 20),
                'university_id': 4,  # МФТИ
                'enrollment_year': 2020
            },
            {
                'full_name': 'Белов Артем Викторович',
                'birth_date': date(2000, 4, 8),
                'university_id': 5,  # ВШЭ
                'enrollment_year': 2018
            },
            {
                'full_name': 'Соколова Юлия Игоревна',
                'birth_date': date(2001, 6, 25),
                'university_id': 5,  # ВШЭ
                'enrollment_year': 2019
            }
        ]

        students_created = 0
        for student_data in students_data:
            if not Student.query.filter_by(full_name=student_data['full_name']).first():
                student = Student(**student_data)
                db.session.add(student)
                students_created += 1

        if students_created > 0:
            print(f"✅ Created {students_created} students")
        else:
            print("ℹ️ Students already exist")

        db.session.commit()
        print("🎉 Database initialization completed successfully!")

if __name__ == '__main__':
    init_db()