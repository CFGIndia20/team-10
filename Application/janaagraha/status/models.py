from django.db import models

# Create your models here.

STATUS = (
    ('unresolved', 'unresolved'),
    ('assigned', 'assigned'),
    ('resolved', 'resolved')
)

class Status(models.Model):
    Title = models.CharField(max_length = 80)
    img = models.ImageField(upload_to = 'pics/')
    desc = models.TextField()
    location = models.CharField(max_length = 80)
    categories = models.TextField()
    stat = models.CharField(choices=STATUS, max_length = 20)
    