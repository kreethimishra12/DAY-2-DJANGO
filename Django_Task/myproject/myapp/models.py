

# Create your models here.
from django.db import models


class Asset(models.Model):
    asset_id=models.CharField(max_length=50)
    asset_name=models.CharField(max_length=50)
    asset_stat=models.CharField(max_length=50)
    segment_id=models.CharField(max_length = 50)
    route_id=models.CharField(max_length=50)
    route_name=models.CharField(max_length=50)
    route_class=models.CharField(max_length=50)
    county_id=models.CharField(max_length=50,default='secondary')
    division_id=models.CharField(max_length=50)
