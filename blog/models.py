from django.db import models
from django.urls import reverse

# Create your models here.

#Every blog should have a title, an author and a body

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(   #we’re using a ForeignKey which allows for a many-to-one relationship. This means that a given user can be the author of many different blog posts
    'auth.User',
    on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail',args=[str(self.id)]) #reference an onject by its url template name, from blog/urls.py
        #we must also use the primary key,self.id,so in this case it will return to posts/1