from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField
from froala_editor.fields import FroalaField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name 
    
    def get_absolute_url(self):
        return reverse("landing")

class Profile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete = models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null = True, blank = True, upload_to = "images/profile/")
    website_url = models.CharField(max_length=225 , null = True , blank = True)
    instagram_url = models.CharField(max_length=225 , null = True , blank = True)


    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("landing")



class Post(models.Model):
    title = models.CharField(max_length=225)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    #category = models.CharField(max_length=225 )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null = True)
    #body = models.TextField()
    body = FroalaField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    header_image = models.ImageField(null = True, blank = True, upload_to = "images/")
    

    def __str__(self):
        return self.title + '|' + str(self.author)
    
    def get_absolute_url(self):
        return reverse("landing")
    
    def total_likes(self):
        return self.likes.count()
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post,related_name = "comments" , on_delete=models.CASCADE)
    name = models.CharField(max_length = 225)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '%s - %s' % (self.post.title , self.name)