from django.db import models

class University(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="Полное название")
    short_name = models.CharField(max_length=50, verbose_name="Сокращенное название")
    established_date = models.DateField(verbose_name="Дата создания")

    def __str__(self):
        return self.short_name

class Student(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    birth_date = models.DateField(verbose_name="Дата рождения")
    university = models.ForeignKey(University, on_delete=models.CASCADE, verbose_name="Университет")
    enrollment_year = models.PositiveIntegerField(verbose_name="Год поступления")

    def __str__(self):
        return self.full_name
