from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Complaints(models.Model):
    user = models.ForeignKey(User, related_name='complaints', on_delete=models.CASCADE,null=True, blank=True)
    Topic = models.CharField(max_length=200)
    img = models.ImageField(null=True)
    categories = models.CharField(max_length=50,null=True)
    location = models.CharField(max_length=50)
    userid = models.CharField(max_length=50,null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True ,blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.Topic

    def get_absolute_url(self):
        return reverse("complaints:shareurl", kwargs={"id": self.id})

STATUS = (
    ('unresolved', 'unresolved'),
    ('assigned', 'assigned'),
    ('resolved', 'resolved')
)

class Status(models.Model):
    complain = models.ForeignKey("Complaints", related_name="statuses", on_delete=models.CASCADE,null=True)
    stat = models.CharField(choices=STATUS, max_length = 20)
    statText = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True,blank=True, null=True)



