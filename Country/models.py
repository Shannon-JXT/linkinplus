from django.db import models

# Create your models here.
class Country(models.Model):
    country_name = models.CharField(max_length=100)
    country_info = models.TextField()
    country_info1 = models.TextField()
    country_info2 = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.country_name

class Region(models.Model):
    region_name = models.CharField(max_length=50)
    migrant_num = models.IntegerField(default=0)
    country_name = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    year = models.IntegerField(default=1996)

    def __str__(self):
        return "<Region: %s  Migrant: %s>" % (self.region_name, self.migrant_num)
