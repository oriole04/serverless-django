#from typing import ContextManager
from django.conf import settings
from django.db import models
from django.db.models import Q
from django.utils import timezone
# Create your models here.  Each definition in the class will be in the database

class BlogPost(models.Model):       #blogpost_set -> query set associated with user
# id = models.IntegerField()  #pk
#    user        = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)  #CASCADE eliminates entirety, or use SET_DEFAULT
#    image       = models.ImageField(upload_to='image/', blank=True, null=True)
    title       = models.CharField(max_length=120)
    slug        = models.SlugField(unique=True)   #Hello World -> Hello-World
    content     = models.TextField(null=True, blank=True)
    description = models.CharField(max_length=180, null = True)
#    price       = models.DecimalField(max_digits=1000,decimal_places=2)
#    summary     = models.TextField(blank=False,null=False)
    featured    = models.BooleanField(default=False)
    publish_date    = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    # objects = BlogPostManager()
    
    class Meta:
        ordering = ['-publish_date', '-updated', '-timestamp']

    def get_absolute_url(self):
        return f"/blog/{self.slug}"
    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"     
    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"
    

#class Blog:
#    title   = 'Hello World'
#    content = 'Something Cool'