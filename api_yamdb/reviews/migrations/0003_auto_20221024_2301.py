# Generated by Django 2.2.16 on 2022-10-24 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20221024_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='confirmation_code',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('admin', 'Администратор'), ('moderator', 'Модератор'), ('user', 'Пользователь')], default='user', max_length=9, verbose_name='Роль пользователя'),
        ),
    ]