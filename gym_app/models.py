from django.db import models
from django.urls import reverse # new

# Create your models here.
class Gym(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    year_established = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('gym_detail', args=[str(self.id)])

class Member(models.Model):
    name = models.CharField(max_length=200)
    dob = models.DateField()
    gym = models.ForeignKey(
        Gym,
        on_delete=models.CASCADE,
    )
    bmi = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('member_detail', args=[str(self.id)])

class Equipment(models.Model):
    name = models.CharField(max_length=200)
    value = (models.PositiveIntegerField())
    gym = models.ForeignKey(
        Gym,
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('equip_detail', args=[str(self.id)])
