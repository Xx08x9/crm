from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Faculty(models.Model):
    name = models.CharField('Название', max_length=255, unique=True)
    short_name = models.CharField('Сокращённое название', max_length=50, unique=True)
    dean = models.CharField('Декан', max_length=255)

    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'
        ordering = ['name']

    def __str__(self):
        return self.short_name


class Direction(models.Model):
    code = models.CharField('Код', max_length=20, unique=True)
    name = models.CharField('Название', max_length=255)
    faculty = models.ForeignKey(
        Faculty,
        on_delete=models.PROTECT,
        related_name='directions',
        verbose_name='Факультет',
    )
    duration = models.PositiveSmallIntegerField(
        'Срок обучения (лет)',
        validators=[MinValueValidator(1), MaxValueValidator(6)],
    )

    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'
        ordering = ['code']

    def __str__(self):
        return f'{self.code} {self.name}'


class Group(models.Model):
    name = models.CharField('Название', max_length=50, unique=True)
    direction = models.ForeignKey(
        Direction,
        on_delete=models.PROTECT,
        related_name='groups',
        verbose_name='Направление',
    )
    admission_year = models.PositiveSmallIntegerField(
        'Год набора',
        validators=[MinValueValidator(2000), MaxValueValidator(2100)],
    )
    is_active = models.BooleanField('Активна', default=True)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ['-admission_year', 'name']

    def __str__(self):
        return self.name
