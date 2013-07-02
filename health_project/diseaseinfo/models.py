from django.db import models
from userinfo.models import UserInfo
# Create your models here.

class Diseases(models.Model):
    disease = models.CharField(max_length=100)
    def __unicode__(self):
        return unicode(self.disease)
        
class DiseaseInfo(models.Model):
    disease_name = models.ForeignKey(Diseases)
    disease_from = models.DateField()
    patient = models.ForeignKey(UserInfo)
    
    def __unicode__(self):
        return unicode(self.disease_name)
