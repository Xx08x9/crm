from django.contrib.auth.models import AbstractUser
from django.db import models


class Student(AbstractUser):
    student_id = models.CharField('Номер студенческого билета', max_length=20, unique=True)
    middle_name = models.CharField('Отчество', max_length=150, blank=True)
    birth_date = models.DateField('Дата рождения', null=True, blank=True)
    phone = models.CharField('Телефон', max_length=20, blank=True)
    group = models.ForeignKey(
        'academics.Group',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='students',
        verbose_name='Группа',
    )

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f'{self.last_name} {self.first_name} ({self.student_id})'
