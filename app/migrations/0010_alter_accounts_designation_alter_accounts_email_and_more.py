# Generated by Django 4.1.5 on 2023-01-30 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_accounts_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='designation',
            field=models.CharField(max_length=55),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='name',
            field=models.CharField(max_length=55),
        ),
    ]
