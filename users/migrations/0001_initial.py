# Generated by Django 3.2.9 on 2021-11-25 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
