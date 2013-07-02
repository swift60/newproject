from django.shortcuts import RequestContext
from django.shortcuts import render_to_response
from diseaseinfo.forms import SearchForm
from diseaseinfo.models import DiseaseInfo,Diseases
import datetime
import json
from django.http import HttpResponse


def search_disease(request):
    '''return the search form  to the index page'''
    form = SearchForm()
    context = {'form':form}
    return render_to_response('search.html', context, context_instance = RequestContext(request))

def search_ajax(request):
    '''autocomplete function 
    input:ajax request
    return json values'''
    if request.is_ajax():
        q = request.GET.get('term', '')    
        diseases= Diseases.objects.filter(disease__contains=q)
        result = []
        for disease in diseases:
            disease_json={}
            disease_json['label']=disease.disease
            disease_json['value']=disease.disease
            result.append(disease_json)
        data = json.dumps(result)
       
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
 

def disease(request):
    '''input:disease name is the input
    output:returns the list of people having that disease,
    if input is multi disease seperated by comma
    return the list of people having multiple disease
    filtering is done cities and agelimits are the filters'''
    form = SearchForm()
    
    age_dict={'infant':[0,5],'children':[6,18],'adult':[19,40],'senior-adult':[41,60],'old':[60,100]}
    city = {'srinagar':'srinagar','anantnag':'anantnag','baramulla':'baramulla'}
    if request.method == "GET":
            disease_name = request.GET['search_text'or None]
            cities=request.GET.getlist('citylist'or None)
            agelimits = request.GET.getlist('agelist'or None)
            if disease_name:
                value=disease_name.split(',')
                if len(value)== 1:
                    disease= DiseaseInfo.objects.filter(disease_name__disease__in=value).order_by('patient')
                    
                    bit= datetime.date.today()
                    if cities:
                        disease=disease.filter(patient__district__in=cities).order_by('patient')
                    if agelimits:
                        agelist=[]
                        agelist=set(agelist)
                        for i in agelimits:
                            agelist2 =[]
                            agelist2=range((age_dict[i])[0],(age_dict[i])[1])
                            agelist2=set(agelist2)
                            agelist=agelist.union(agelist2)
                            
                        agel = []
                        for i in disease:
                            if i.patient.age in agelist:
                                agel.append(i.patient)
                        disease = disease.filter(patient__in=agel).order_by('patient') 
                    if disease:    
                        disease_javascript ={}
                        for dis in disease:
                            disease_json={}
                            result=[]
                            disease_json['name']=dis.patient.firstname
                            disease_json['lat']=dis.patient.lat
                            disease_json['lng']=dis.patient.lng
                            disease_json['district']=dis.patient.district
                            disease_json['pic']=dis.patient.pic.url
                            disease_json['lastname']=dis.patient.lastname
                            disease_json['address']=dis.patient.address
                            disease_json['zip']=dis.patient.zip
                            result.append(disease_json)
                            disease_javascript[dis.patient.id]=result
                        disease_java=json.dumps(disease_javascript)
                    else:
                        disease_javascript={}
                        disease_java=json.dumps(disease_javascript)
                    return render_to_response('disease_statistic.html', {'disease':disease,'bit':bit,'age_dict':age_dict,'city':city,'disease_name':disease_name,'cities':cities,'agelimits':agelimits,'results':disease_java,'form':form},context_instance = RequestContext(request))
                        
                else:
                    disease= DiseaseInfo.objects.filter(disease_name__disease=value[0])
                    lst = []
                    for i in disease:
                        lst.append(i.patient)
                        if len(value)>1:
                            for i in value[1:]:
                                disease = DiseaseInfo.objects.filter(disease_name__disease=i)
                                klist =[]
                                for j in disease:
                                    klist.append(j.patient)
                                set(lst).intersection(set(klist))
                        disease = DiseaseInfo.objects.filter(patient__in=lst).filter(disease_name__disease__in=value)
                        bit= datetime.date.today()
                        if cities:
                            disease=disease.filter(patient__district__in=cities)
                    if agelimits:
                        agelist=[]
                        agelist=set(agelist)
                        for i in agelimits:
                            agelist2=(range((age_dict[i])[0],(age_dict[i])[1]))
                            agelist2=set(agelist2)
                            agelist=agelist.union(agelist2)
                        agel = []
                        for i in disease:
                            if i.patient.age in agelist:
                                agel.append(i.patient)
                        disease = disease.filter(patient__in=agel) 
                    if disease:    
                        disease_javascript ={}
                        for dis in disease:
                            disease_json={}
                            result=[]
                            disease_json['name']=dis.patient.firstname
                            disease_json['lat']=dis.patient.lat
                            disease_json['lng']=dis.patient.lng
                            disease_json['district']=dis.patient.district
                            disease_json['pic']=dis.patient.pic.url
                            disease_json['lastname']=dis.patient.lastname
                            
                            result.append(disease_json)
                            disease_javascript[dis.patient.id]=result
                        disease_java=json.dumps(disease_javascript)
                    else:
                        disease_javascript={}
                        disease_java=json.dumps(disease_javascript)
                    return render_to_response('disease_statistic.html', {'disease':disease,'bit':bit,'age_dict':age_dict,'city':city,'disease_name':disease_name,'cities':cities,'agelimits':agelimits,'results':disease_java,'form':form},context_instance = RequestContext(request))
            else:
                return render_to_response('disease_statistic.html', {'form':form},context_instance = RequestContext(request))
          


    
      


       
