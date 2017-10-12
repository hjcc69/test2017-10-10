from django.db import models
from django.contrib.auth.models import User




class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to= "media", blank=True)


    def __unicode__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User)
    product = models.ForeignKey(Product)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.content