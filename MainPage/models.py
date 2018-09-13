from django.db import models

# Create your models here.

class HomePageInfo(models.Model):
    intro_text = models.CharField(max_length=150, default="Default Value")
    project_one = models.CharField(max_length=250, default="Default Value")
    project_two = models.CharField(max_length=250, default="Default Value")
    project_three = models.CharField(max_length=250, default="Default Value")
    project_four = models.CharField(max_length=250, default="Default Value")
    project_five = models.CharField(max_length=250, default="Default Value")
    project_six = models.CharField(max_length=250, default="Default Value")
    project_seven = models.CharField(max_length=250, default="Default Value")

    def __str__(self):
        return self.intro_text
