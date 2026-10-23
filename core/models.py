from django.db import models

# Create your models here.

class Profile(models.Model):
    image = models.ImageField(upload_to='profile_image')
    languages = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    about = models.TextField(max_length=1000)

class Hobbie(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='hobbie_image')
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name="hobbies")

    def __str__(self):
        return self.name
        

class Project(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='project_image')
    url = models.CharField(max_length=200)
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name="projects")

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='contact_image')
    url = models.CharField(max_length=200)
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name="contacts")


    def __str__(self):
        return self.name

class CodeLanguage(models.Model):
    name = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name="codes")

    def __str__(self):
            return self.name