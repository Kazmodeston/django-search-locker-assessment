from django.db import models

# Create your models here.

class Locker(models.Model):
    city = models.CharField(max_length = 200, null=False, blank=False)
    state = models.CharField(max_length = 200, null=False, blank=False)
    locker_name = models.CharField(max_length = 200, null=False, blank=False)
    price_description = models.TextField()
    locker_description = models.TextField()
    date    = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length = 100, null=False, blank=False)
    featured = models.TextField(null=True)

    def __str__(self):
        return self.state