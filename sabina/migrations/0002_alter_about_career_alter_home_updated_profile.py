# Generated by Django 4.0.1 on 2022-02-09 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sabina', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='career',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='home',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_name', models.CharField(max_length=10)),
                ('link', models.URLField()),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sabina.about')),
            ],
        ),
    ]
