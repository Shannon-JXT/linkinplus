from django.db import models

# Create your models here.
class Country(models.Model):
    country_name = models.CharField(max_length=100)
    country_info = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    lats_updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "<Country: %s>" % self.country_name
