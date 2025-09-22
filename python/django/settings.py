version: '3.8'

services:
  db:
    image: mysql:8.0
    container_name: django_mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: django_db
      MYSQL_USER: django_user
      MYSQL_PASSWORD: django_password
    ports:
      - "3306:3306"
    volumes:
      - db_data:/var/lib/mysql

volumes:
  db_data:

# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_db',
        'USER': 'django_user',
        'PASSWORD': 'django_password',
        'HOST': 'db',
        'PORT': '3306',
    }
}