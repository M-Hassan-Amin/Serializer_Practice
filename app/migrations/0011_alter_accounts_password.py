# Generated by Django 4.1.5 on 2023-01-30 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_accounts_designation_alter_accounts_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='password',
            field=models.TextField(),
        ),
    ]
