# Generated by Django 4.1.5 on 2023-01-30 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_student_joined_on'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=55)),
                ('designation', models.CharField(default='', max_length=55)),
                ('email', models.EmailField(default='', max_length=254, unique=True)),
                ('password', models.CharField(default='', max_length=55)),
            ],
        ),
    ]