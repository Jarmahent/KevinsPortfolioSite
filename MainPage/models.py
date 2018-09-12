from django.db import models

# Create your models here.

class HomePageInfo(models.Model):
    intro_text = models.CharField(max_length=150)

    # project_one = models.CharField(max_length=50)
    # project_two = models.CharField(max_length=50)
    # project_three = models.CharField(max_length=50)
    # project_four = models.CharField(max_length=50)
    # project_five = models.CharField(max_length=50)
    # project_six = models.CharField(max_length=50)
    # project_seven = models.CharField(max_length=50)

    def __str__(self):
        return self.intro_text
