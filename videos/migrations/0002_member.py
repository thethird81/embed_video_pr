# Generated by Django 4.2.2 on 2023-07-13 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=200)),
                ('passwd', models.CharField(max_length=50)),
                ('age', models.IntegerField(max_length=50)),
            ],
        ),
    ]