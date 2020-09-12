from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_recruiter = models.BooleanField(default = False)
    is_jobseeker = models.BooleanField(default = False )

    def __str__(self):
        return self.username

class Recruiter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    company = models.CharField(max_length=25)
    location = models.CharField(max_length=30)
    bio = models.TextField(blank=True)
    def __str__(self):
        return self.name
    
class Jobseeker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=20)
    email = models.EmailField()
    phonenumber = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class JobPost(models.Model):
    company = models.CharField(max_length =100)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    position  = models.CharField(max_length=100)
    location = models.CharField(max_length=20)
    min_salary = models.PositiveIntegerField()
    max_salary = models.PositiveIntegerField()
    experience = models.PositiveIntegerField()
    def __str__(self):
        return self.position





class Applied(models.Model):
    pass 

class Shortlisted(models.Model):
    pass 

