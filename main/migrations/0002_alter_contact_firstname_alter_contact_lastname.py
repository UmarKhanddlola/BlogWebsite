# Generated by Django 5.0.3 on 2024-03-26 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='FirstName',
            field=models.CharField(help_text='Enter field documentation', max_length=122),
        ),
        migrations.AlterField(
            model_name='contact',
            name='LastName',
            field=models.CharField(help_text='Enter field doccumentation', max_length=122),
        ),
    ]
