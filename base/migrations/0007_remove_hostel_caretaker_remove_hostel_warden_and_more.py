# Generated by Django 4.0.6 on 2023-03-02 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_hostel_capacity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostel',
            name='caretaker',
        ),
        migrations.RemoveField(
            model_name='hostel',
            name='warden',
        ),
        migrations.AddField(
            model_name='caretaker',
            name='hostel',
            field=models.ForeignKey(default='Z', on_delete=django.db.models.deletion.CASCADE, to='base.hostel'),
        ),
        migrations.AddField(
            model_name='student',
            name='hostel',
            field=models.ForeignKey(default='Z', on_delete=django.db.models.deletion.CASCADE, to='base.hostel'),
        ),
        migrations.AddField(
            model_name='warden',
            name='hostel',
            field=models.ForeignKey(default='Z', on_delete=django.db.models.deletion.CASCADE, to='base.hostel'),
        ),
    ]
