# Generated by Django 3.2.16 on 2025-01-14 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_citysalarydynamicsprof_citysalaryshareprof'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalaryDynamycsAll_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(unique=True, verbose_name='Год')),
                ('avg_salary', models.IntegerField(verbose_name='Средняя зарплата')),
                ('vacancy_count', models.IntegerField(verbose_name='Количество вакансий')),
            ],
        ),
    ]
