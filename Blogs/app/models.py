from django.db import models

# Create your models here.
class BlogData(models.Model):
    title = models.TextField(max_length=200,null=False,blank=False)
    time = models.TimeField()
    description = models.TextField(max_length=5000,null=False,blank=False)

    def __str__(self):
        return self.title