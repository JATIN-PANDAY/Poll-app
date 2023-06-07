from django.db import models

# Create your models here.

class Poll(models.Model):
    question = models.CharField(max_length=200)
    option_A = models.CharField(max_length=100)
    option_B = models.CharField(max_length=100)
    option_C = models.CharField(max_length=100)
    option_A_count = models.IntegerField(default=0)
    option_B_count = models.IntegerField(default=0)
    option_C_count = models.IntegerField(default=0)

