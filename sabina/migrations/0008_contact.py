# Generated by Django 4.0.1 on 2022-03-25 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sabina', '0007_delete_contact'),
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
    ]