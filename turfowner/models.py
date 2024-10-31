from django.db import models

# Create your models here.


class turf_table(models.Model):
   
    image=models.ImageField(default="img.png",upload_to='turfimages')
    name=models.CharField(max_length=150,blank=False)
    game_type = models.TextField()
    location=models.TextField(blank=False)
    locaion_url=models.TextField()
    open_time=models.TimeField()
    close_time=models.TimeField()
    rent=models.CharField(max_length=5,default=0)
    discription=models.TextField()
    courts=models.IntegerField()
    slots=models.BooleanField(default=True)
