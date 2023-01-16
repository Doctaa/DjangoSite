# Generated by Django 3.0.14 on 2023-01-15 22:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_auto_20230114_1945'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime(2023, 1, 16, 0, 18, 2, 974336), verbose_name='Дата заказа')),
                ('num_table', models.PositiveIntegerField(verbose_name='Номер стола')),
                ('name', models.CharField(max_length=22, null=True, verbose_name='Имя клиента')),
            ],
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.AlterField(
            model_name='table',
            name='shape',
            field=models.CharField(choices=[('rectangular', 'Прямоугольный'), ('oval', 'Овальный')], max_length=50, verbose_name='Форма стола'),
        ),
    ]
