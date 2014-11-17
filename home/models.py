from django.db import models

class Testers(models.Model):
    email = models.EmailField(max_length=150, unique=True)
    ip = models.CharField(max_length=20)
    agent = models.TextField(max_length=500)
    time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.email
