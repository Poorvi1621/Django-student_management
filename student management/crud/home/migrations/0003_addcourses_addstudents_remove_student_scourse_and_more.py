# Generated by Django 4.1.3 on 2022-12-27 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddCourses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=100)),
                ('fees', models.IntegerField()),
                ('duration', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='AddStudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=100)),
                ('semail', models.EmailField(max_length=100)),
                ('smobile', models.CharField(max_length=10)),
                ('saddress', models.CharField(max_length=255)),
                ('scollege', models.CharField(max_length=255)),
                ('sdegree', models.CharField(max_length=100)),
                ('total_amount', models.IntegerField()),
                ('paid_amount', models.IntegerField()),
                ('due_amount', models.FloatField()),
                ('scourse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.addcourses')),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='scourse',
        ),
        migrations.DeleteModel(
            name='courses',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]