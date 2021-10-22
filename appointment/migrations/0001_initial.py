# Generated by Django 3.2.7 on 2021-10-22 18:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='static/', verbose_name='Изображение')),
                ('name', models.CharField(max_length=50, verbose_name='Фамилия Имя Отчество')),
                ('specialty', models.CharField(max_length=50, verbose_name='Специальность')),
                ('work_experience', models.CharField(max_length=50, verbose_name='Опыт работы')),
            ],
        ),
        migrations.CreateModel(
            name='DateRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Дата приема')),
                ('weekday', models.CharField(blank=True, max_length=50, null=True, verbose_name='День недели')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150, verbose_name='Ф.И.О')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('insurance', models.CharField(max_length=20, verbose_name='Страховой полис')),
                ('time_record_create', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient_record', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='TimeRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(verbose_name='Время приема')),
                ('date_now', models.DateTimeField(auto_now_add=True)),
                ('recorded', models.BooleanField(default=False)),
                ('card', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='card_time', to='appointment.card', verbose_name='Врач')),
                ('daterecord', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='timerecord', to='appointment.daterecord', verbose_name='Дата приема')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='time_patient', to='appointment.patient', verbose_name='Пациент')),
            ],
        ),
    ]
