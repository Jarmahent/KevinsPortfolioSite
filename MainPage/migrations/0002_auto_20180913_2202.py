# Generated by Django 2.0.1 on 2018-09-13 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepageinfo',
            name='project_five',
            field=models.CharField(default='Default Value', max_length=250),
        ),
        migrations.AlterField(
            model_name='homepageinfo',
            name='project_four',
            field=models.CharField(default='Default Value', max_length=250),
        ),
        migrations.AlterField(
            model_name='homepageinfo',
            name='project_one',
            field=models.CharField(default='Default Value', max_length=250),
        ),
        migrations.AlterField(
            model_name='homepageinfo',
            name='project_seven',
            field=models.CharField(default='Default Value', max_length=250),
        ),
        migrations.AlterField(
            model_name='homepageinfo',
            name='project_six',
            field=models.CharField(default='Default Value', max_length=250),
        ),
        migrations.AlterField(
            model_name='homepageinfo',
            name='project_three',
            field=models.CharField(default='Default Value', max_length=250),
        ),
        migrations.AlterField(
            model_name='homepageinfo',
            name='project_two',
            field=models.CharField(default='Default Value', max_length=250),
        ),
    ]
