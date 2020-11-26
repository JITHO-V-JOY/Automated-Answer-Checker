# Generated by Django 3.1.2 on 2020-11-26 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerKeys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=256)),
                ('answer_key', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='AnswerSheets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_number', models.IntegerField()),
                ('student_name', models.CharField(max_length=256)),
                ('subject_name', models.CharField(max_length=256)),
                ('answer_sheet', models.FileField(upload_to='documents/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=32)),
                ('answersheet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.answersheets')),
            ],
        ),
    ]
