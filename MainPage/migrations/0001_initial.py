# Generated by Django 2.0.1 on 2018-09-13 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intro_text', models.CharField(default='Default Value', max_length=150)),
                ('project_one', models.CharField(default='Default Value', max_length=180)),
                ('project_two', models.CharField(default='Default Value', max_length=180)),
                ('project_three', models.CharField(default='Default Value', max_length=180)),
                ('project_four', models.CharField(default='Default Value', max_length=180)),
                ('project_five', models.CharField(default='Default Value', max_length=180)),
                ('project_six', models.CharField(default='Default Value', max_length=180)),
                ('project_seven', models.CharField(max_length=180)),
            ],
        ),
    ]
