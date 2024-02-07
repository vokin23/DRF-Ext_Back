from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from rest_framework.exceptions import ValidationError


class Works(models.Model):
    name_work = models.CharField(max_length=30, blank=False, null=False, verbose_name='Наименование должности')
    max_workers = models.PositiveIntegerField()
    zarplata = models.FloatField(max_length=15, blank=False, null=False)

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.name_work


class Workers(models.Model):
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    otchestvo = models.CharField(max_length=20)
    date_rojdenia = models.DateField()
    work = models.ForeignKey(Works, on_delete=models.CASCADE)
    stavka = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1)
        ]
    )
    salary = models.FloatField(editable=False)

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'{self.first_name} {self.second_name} {self.otchestvo}'

    def save(self, *args, **kwargs):
        if self.work:
            self.salary = float(self.work.zarplata) * float(self.stavka)  # Вычисляем зарплату

        super(Workers, self).save(*args, **kwargs)
