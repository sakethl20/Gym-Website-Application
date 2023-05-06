from django.db import models

class Customer(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email =  models.EmailField()

    def __str__(self):
        return f'{self.firstname}, {self.lastname}, {self.email}' 

class Programs(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    timings = models.TextField()

    def __str__(self):
        return f'{self.title}, {self.description}, {self.timings}' 
    
class SignedProgram(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    programName =  models.CharField(max_length=50)

    def __str__(self):
        return f'{self.firstname}, {self.lastname}, {self.programName}'