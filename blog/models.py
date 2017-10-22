from django.db import models

from django.utils import timezone


class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

    
class Post(models.Model):
    
    author=models.ForeignKey('auth.User')
    title=models.CharField(max_length=200)
    text=models.TextField()
    slug=models.SlugField(max_length=200,unique=False)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    modified=models.DateTimeField(auto_now=True)
   
    #create_date=models.DateTimeField(default=timezone.now)
    #published_date=models.DateTimeField(blank=True,null=True)
    def publish(self):
        
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title


