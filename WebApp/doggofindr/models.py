from django.db import models
from django.contrib.auth.models import User
#database for image table
class Image(models.Model):
    imgName = models.CharField(max_length=200, null=True, blank=True) #Image name
    breedName = models.CharField(max_length=200, null=True, blank=True)
    imgFile = models.FileField(null=True, blank=True) #image url
    accuracy = models.FloatField(null=True, default=0)
    author = models.ForeignKey(User,null=True)
    def __str__(self):
        return str(self.imgFile)
