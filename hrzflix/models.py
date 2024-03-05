from django.db import models
import datetime
from django.contrib.auth.models import User
import os

def getfilename(request,filename):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename = "%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)

class Genre(models.Model):
    name = models.CharField(max_length=15,null=False,blank=False)
    create_at = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return self.name

class Theme(models.Model):
    name = models.CharField(max_length=15,null=False,blank=False)
    create_at = models.DateTimeField(auto_now_add =True)

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        # Check if the number of existing instances is less than 3
        if Theme.objects.count() >= 3:
            raise ValidationError("Cannot create more than 3 themes.")
        super().save(*args, **kwargs)

class Movie(models.Model):
    genre=models.ForeignKey(Genre,on_delete=models.CASCADE)
    theme=models.ForeignKey(Theme,on_delete=models.CASCADE)
    name = models.CharField(max_length=20,null=False,blank=False)
    movie_image = models.ImageField(upload_to=getfilename,blank=False)
    trailer_url = models.URLField(max_length=100,null=True,blank=True,default='https://youtu.be/TcMBFSGVi1c?si=czodo3KRTSWrj2U-')
    description = models.CharField(max_length=100,blank=False,null=False)
    rating = models.FloatField(null=False,blank=False)
    duration = models.CharField(max_length=20,null=False,blank=False)
    age = models.CharField(max_length=20,null=False,blank=False)
    trending = models.BooleanField(default=False,help_text="1-show 0-hidden")
    create_at = models.DateTimeField(auto_now_add = True)
    

    def __str__(self):
        return self.name

class WatchLater(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    movies = models.ForeignKey(Movie,on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add = True)

class Fav(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)    
    movies = models.ForeignKey(Movie,on_delete=models.CASCADE)    
    create_at = models.DateTimeField(auto_now_add=True)

class Slider(models.Model):
    theme=models.ForeignKey(Theme,on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=20,null=False,blank=False)
    trailer_url = models.URLField(max_length=100,null=True,blank=True,default='https://youtu.be/TcMBFSGVi1c?si=czodo3KRTSWrj2U-')
    movie_image = models.ImageField(upload_to=getfilename,blank=False)
    description = models.TextField(max_length=81,blank=False,null=False,help_text='Note give only 80 Letters')
    rating = models.FloatField(null=False,blank=False)
    duration = models.CharField(max_length=20,null=False,blank=False)
    age = models.CharField(max_length=20,null=False,blank=False)
    create_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.name
