from django.db import models

# Create your models here.
class Usuarios(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=20)
    salt = models.CharField(max_length=50)
    hash = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Listas(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    date = models.DateField()
    parentUserId = models.ForeignKey(Usuarios, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Tareas(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=100)
    release_date = models.TimeField(auto_now=False, auto_now_add=False)
    done = models.BooleanField (default=False)
    parentListID =  models.ForeignKey(Listas, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text