from django.db import models

# Create your models here.


# after error
class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name