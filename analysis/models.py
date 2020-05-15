from django.db import models

class Performance(models.Model):
    """
    Performance Metrics Data Model
    """
    date = models.DateField('Date')
    channel = models.CharField('Channel', max_length=50)
    country = models.CharField('Country', max_length=50)
    os = models.CharField('OS', max_length=10)
    impressions =  models.IntegerField('Impressions', default=0)
    clicks =  models.IntegerField('Clicks', default=0)
    installs =  models.IntegerField('Installs', default=0)
    spend = models.DecimalField('Spend', max_digits=30, decimal_places=3, default=0) 
    revenue = models.DecimalField('Revenue', max_digits=30, decimal_places=3, default=0) 

    @property
    def cpi(self):
        return self.spend / self.installs

