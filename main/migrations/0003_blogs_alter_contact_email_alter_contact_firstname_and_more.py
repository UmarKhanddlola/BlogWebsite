# Generated by Django 5.0.3 on 2024-03-26 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_contact_firstname_alter_contact_lastname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BlogTitle', models.CharField(max_length=122)),
                ('BlogContent', models.CharField(max_length=122)),
                ('BlogPublishDate', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='Email',
            field=models.EmailField(max_length=122),
        ),
        migrations.AlterField(
            model_name='contact',
            name='FirstName',
            field=models.CharField(max_length=122),
        ),
        migrations.AlterField(
            model_name='contact',
            name='LastName',
            field=models.CharField(max_length=122),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Message',
            field=models.CharField(max_length=112),
        ),
    ]
