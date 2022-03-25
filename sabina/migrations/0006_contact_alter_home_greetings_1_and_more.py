# Generated by Django 4.0.1 on 2022-03-25 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sabina', '0005_alter_education_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='home',
            name='greetings_1',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='home',
            name='greetings_2',
            field=models.CharField(max_length=15),
        ),
    ]