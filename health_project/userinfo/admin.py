from django.contrib import admin
from userinfo.models import UserInfo
from diseaseinfo.models import DiseaseInfo,Diseases
from health_project import settings
from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin

class DiseaseInline(admin.TabularInline):
    model = Diseases

class DiseaseInfoInline(admin.StackedInline):
    model= DiseaseInfo
  
  

class UserInfoAdmin(admin.ModelAdmin):
    inlines =[DiseaseInfoInline,]

class DiseasesAdmin(AjaxSelectAdmin):
    form = make_ajax_form(DiseaseInfo,{'disease_name':'person'})

admin.site.register(UserInfo,UserInfoAdmin)
admin.site.register(DiseaseInfo,DiseasesAdmin)
admin.site.register(Diseases)

