# Generated by Django 3.0.4 on 2020-04-11 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passsystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passes',
            name='pass_people_count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='passes',
            name='pass_user_aadhar_number',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='passes',
            name='pass_user_phonenumber',
            field=models.IntegerField(),
        ),
    ]
