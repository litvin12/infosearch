"""
Django Models (Модели)

Модели определяют структуру данных и автоматически создают таблицы в БД.
Один класс = одна таблица.

Django ORM (Object-Relational Mapping):
- Избавляет от написания SQL вручную
- Автоматически создаёт миграции (изменения схемы)
- Обеспечивает защиту от SQL-injection
"""

from django.db import models

# ============================================================
# МОДЕЛИ (Models)
# ============================================================

class University(models.Model):
    """
    Модель университета.
    
    Автоматически создаёт таблицу с полями:
    - id (INTEGER PRIMARY KEY) — создаётся автоматически
    - full_name (VARCHAR 255)
    - short_name (VARCHAR 50)
    - established_date (DATE)
    
    Миграция:
    python manage.py makemigrations
    python manage.py migrate
    """
    
    full_name = models.CharField(
        max_length=255, 
        verbose_name="Полное название"
    )
    
    short_name = models.CharField(
        max_length=50, 
        verbose_name="Сокращенное название"
    )
    
    established_date = models.DateField(
        verbose_name="Дата создания"
    )

    def __str__(self):
        """
        Строковое представление объекта.
        Используется в админ-панели и при выводе в консоли.
        """
        return self.short_name

    class Meta:
        """Метаинформация о модели (используется админ-панелью)"""
        verbose_name = "Университет"
        verbose_name_plural = "Университеты"


class Student(models.Model):
    """
    Модель студента.
    
    Автоматически создаёт таблицу с полями:
    - id (INTEGER PRIMARY KEY) — создаётся автоматически
    - full_name (VARCHAR 255)
    - birth_date (DATE)
    - university_id (INTEGER FOREIGN KEY) — ссылка на University
    - enrollment_year (INTEGER)
    
    Связь: Many-to-One (многие студенты → один университет)
    """
    
    full_name = models.CharField(
        max_length=255, 
        verbose_name="ФИО"
    )
    
    birth_date = models.DateField(
        verbose_name="Дата рождения"
    )
    
    # Foreign Key: связь с таблицей University
    # on_delete=models.CASCADE: при удалении университета удаляются его студенты
    university = models.ForeignKey(
        University, 
        on_delete=models.CASCADE, 
        verbose_name="Университет"
    )
    
    enrollment_year = models.PositiveIntegerField(
        verbose_name="Год поступления"
    )

    def __str__(self):
        """Строковое представление объекта"""
        return self.full_name

    class Meta:
        """Метаинформация о модели"""
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
