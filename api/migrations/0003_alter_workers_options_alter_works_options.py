# Generated by Django 5.0.2 on 2024-02-07 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_workers_salary'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workers',
            options={'verbose_name': 'Работник', 'verbose_name_plural': 'Работники'},
        ),
        migrations.AlterModelOptions(
            name='works',
            options={'verbose_name': 'Работа', 'verbose_name_plural': 'Работы'},
        ),
    ]
