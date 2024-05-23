from django.db import models 
from cloudinary.models import CloudinaryField

# Create your models here.
# models -> module
# Model -> a class defined inside models module
# Post -> child class
# Model -> parent class

# cloudinary

class Post(models.Model): 

    name=models.CharField('name', max_length=20, blank=False, null=False)
    body=models.CharField('body',max_length=50,blank=False,null=False)
    created_at=models.DateTimeField("created_at",blank=True,auto_now_add=True) 
    likes=models.PositiveIntegerField('likes',default=0,blank=True)
    image=CloudinaryField('image',blank=True)



