# Generated by Django 3.1.2 on 2020-11-26 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_delete_answertable'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answerkeys',
            options={'verbose_name_plural': 'Answer Key'},
        ),
        migrations.AlterModelOptions(
            name='answersheets',
            options={'verbose_name_plural': 'Answer Sheet'},
        ),
        migrations.AlterField(
            model_name='answersheets',
            name='roll_number',
            field=models.IntegerField(unique=True),
        ),
    ]
