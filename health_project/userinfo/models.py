from django.db import models
import urllib
from xml.dom import minidom

def coordinate(url):
    page = str(urllib.urlopen(url).read())
    d=minidom.parseString(page)
    coords=d.getElementsByTagName("location")
    for node in coords:
        a1=node.getElementsByTagName('lat')
        a2=node.getElementsByTagName('lng')
        lat,lng= a1[0].childNodes[0].nodeValue,a2[0].childNodes[0].nodeValue
    return lat,lng   
class UserInfo(models.Model):
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    region = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    zip = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    lat = models.FloatField(blank = True, null = True, )
    lng=models.FloatField(blank = True, null = True, )
    pic = models.ImageField(upload_to="images/",blank=True,null=True)
    age = models.IntegerField()
    
    def __unicode__(self):
        return unicode(self.firstname)
    
    def save(self,*args, **kwargs):
        if self.address:
            url="http://maps.google.com/maps/api/geocode/xml?address="
            url= url+self.address+","+self.zip+","+self.district+","+self.region+"&sensor=false"
            print url
            lat,lng=coordinate(url)
            self.lat=lat
            self.lng=lng
        super(UserInfo, self).save(*args, **kwargs)
    

