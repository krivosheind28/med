# Generated by Django 3.2.7 on 2021-10-22 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='daterecord',
            options={'verbose_name': 'Дата приема', 'verbose_name_plural': 'Даты приема'},
        ),
        migrations.AlterModelOptions(
            name='patient',
            options={'verbose_name': 'Пациент', 'verbose_name_plural': 'Пациенты'},
        ),
        migrations.AlterModelOptions(
            name='timerecord',
            options={'verbose_name': 'Время записи', 'verbose_name_plural': 'Время записи'},
        ),
        migrations.RemoveField(
            model_name='patient',
            name='time_record_create',
        ),
        migrations.AlterField(
            model_name='timerecord',
            name='date_now',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания записи'),
        ),
    ]
