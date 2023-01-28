# Generated by Django 4.1.5 on 2023-01-28 09:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_classroom_student_student_classroom'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='joined_on',
            field=models.DateTimeField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='student',
            name='joined_on',
            field=models.DateTimeField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='student',
            name='classroom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_details', to='app.classroom'),
        ),
    ]
