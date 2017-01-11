#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.template import loader, Context
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.shortcuts import render
from django.core.context_processors import csrf
from restaurant.models import *
from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test
import datetime
#Para registro de datos de usuarios.
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404, HttpResponse, HttpResponseRedirect
from forms import *
from django.forms import forms
import recommendations
from recommendations import *
from FIS import expert, FIS, MF, experto, restaurant, correlacion
from django.contrib.auth.models import User
import math
from math import * 
#Para poi list
from django.shortcuts import render
#para add_point
import json
import urllib2
import pyproj
from pyproj import *
import datetime
from datetime import *
#Librerias para la union de listas en entropia.
import heapq
from heapq import merge
import dateutil 
from dateutil.relativedelta import *
from django.core import serializers
import json

#VISTA INICIAL DE LA APLICACION.
def index(request):
    try:
        u = request.user.profile
        user = User.objects.get(id=u.user.id)
        print user
    except:
        u = None 

    t=[]
    
    if request.method == 'POST': 
      if request.user.is_authenticated():   
        u = request.user.profile
        user=u.user.username
        #datajson= json.dumps(json.loads(request.body))
        json_data = json.loads(request.body)
        dropdowntxt=json_data['menutxt']
        tablevalue=json_data['menuval']['0']['value']
        t.append(tablevalue)
        t.append(dropdowntxt)
        #Price range
        if tablevalue=='1':
            print 'entro a 1'
            table = Pricerange.objects.get(type_price=dropdowntxt) 
            query = Restaurant.objects.filter(price_range_id=table.id)
            res = {'restaurant':[{'id': q.id, 'name':q.name, 'address':q.address, 
                                  'description':q.description, 'price': table.type_price, 
                                  'url': q.url, 'phone': q.phone, 'hours':q.hours,'city':q.city, 
                                  'state':q.state, 'country':q.country, 'zipcode':q.zipcode, 
                                  'alcohol': q.alcohol_id, 'dresscode':q.dress_code_id, 
                                  'atmosphere':q.atmosphere_id, 'urlimg':q.urlimg, 
                                  'cuisine': q.cuisine_id, 'parking': q.parking_id, 
                                  'payment': q.payment_id, 'instalation': q.instalation_id }  
                                  for q in query ]}        
        #Instalation
        elif tablevalue=='2':
            print 'entro a 2'
            table = Instalation.objects.get(type_instalation=dropdowntxt) 
            query = Restaurant.objects.filter(instalation_id=table.id)
            res = {'restaurant':[{'id': q.id, 'name':q.name, 'address':q.address, 
                                  'description':q.description, 'price': q.price_range_id, 
                                  'url': q.url, 'phone': q.phone, 'hours':q.hours,'city':q.city, 
                                  'state':q.state, 'country':q.country, 'zipcode':q.zipcode, 
                                  'alcohol': q.alcohol_id, 'dresscode':q.dress_code_id, 
                                  'atmosphere':q.atmosphere_id, 'urlimg':q.urlimg, 
                                  'cuisine': q.cuisine_id, 'parking': q.parking_id, 
                                  'payment': q.payment_id, 'instalation': table.type_instalation }  
                                  for q in query ]}        
        #Parking
        elif tablevalue=='3':
            print 'entro a 3'
            table = Parking.objects.get(type_parking=dropdowntxt)
            query = Restaurant.objects.filter(parking_id=table.id)
            res = {'restaurant':[{'id': q.id, 'name':q.name, 'address':q.address, 
                                  'description':q.description, 'price': q.price_range_id, 
                                  'url': q.url, 'phone': q.phone, 'hours':q.hours,'city':q.city, 
                                  'state':q.state, 'country':q.country, 'zipcode':q.zipcode, 
                                  'alcohol': q.alcohol_id, 'dresscode':q.dress_code_id, 
                                  'atmosphere':q.atmosphere_id, 'urlimg':q.urlimg, 
                                  'cuisine': q.cuisine_id, 'parking': table.type_parking, 
                                  'payment': q.payment_id, 'instalation': q.instalation_id }  
                                  for q in query ]}         
        #Atmosphere
        elif tablevalue=='4':
            print 'entro a 4'
            table = Atmosphere.objects.get(type_atmosphere=dropdowntxt)
            query = Restaurant.objects.filter(atmosphere_id=table.id)
            res = {'restaurant':[{'id': q.id, 'name':q.name, 'address':q.address, 
                                  'description':q.description, 'price': q.price_range_id, 
                                  'url': q.url, 'phone': q.phone, 'hours':q.hours,'city':q.city, 
                                  'state':q.state, 'country':q.country, 'zipcode':q.zipcode, 
                                  'alcohol': q.alcohol_id, 'dresscode':q.dress_code_id, 
                                  'atmosphere':table.type_atmosphere, 'urlimg':q.urlimg, 
                                  'cuisine': q.cuisine_id, 'parking': q.parking_id, 
                                  'payment': q.payment_id, 'instalation': q.instalation_id }  
                                  for q in query ]}         
        #Payment
        elif tablevalue=='5':
            print 'entro a 5'
            table = Payment.objects.get(type_payment=dropdowntxt)
            query = Restaurant.objects.filter(payment_id=table.id)
            res = {'restaurant':[{'id': q.id, 'name':q.name, 'address':q.address, 
                                  'description':q.description, 'price': q.price_range_id, 
                                  'url': q.url, 'phone': q.phone, 'hours':q.hours,'city':q.city, 
                                  'state':q.state, 'country':q.country, 'zipcode':q.zipcode, 
                                  'alcohol': q.alcohol_id, 'dresscode':q.dress_code_id, 
                                  'atmosphere':q.atmosphere_id, 'urlimg':q.urlimg, 
                                  'cuisine': q.cuisine_id, 'parking': q.parking_id, 
                                  'payment': table.type_payment, 'instalation': q.instalation_id }  
                                  for q in query ]}        
        #Dresscode
        elif tablevalue=='6':
            print 'entro a 6'
            table = Dresscode.objects.get(type_dresscode=dropdowntxt)
            query = Restaurant.objects.filter(dress_code_id=table.id)
            res = {'restaurant':[{'id': q.id, 'name':q.name, 'address':q.address, 
                                  'description':q.description, 'price': q.price_range_id, 
                                  'url': q.url, 'phone': q.phone, 'hours':q.hours,'city':q.city, 
                                  'state':q.state, 'country':q.country, 'zipcode':q.zipcode, 
                                  'alcohol': q.alcohol_id, 'dresscode':table.type_dresscode, 
                                  'atmosphere':q.atmosphere_id, 'urlimg':q.urlimg, 
                                  'cuisine': q.cuisine_id, 'parking': q.parking_id, 
                                  'payment': q.payment_id, 'instalation': q.instalation_id }  
                                  for q in query ]}        
            #Alcohol
        elif tablevalue=='7':
            print 'entro a 7'
            table = Alcohol.objects.get(type_alcohol=dropdowntxt)
            query = Restaurant.objects.filter(alcohol_id=table.id)
            res = {'restaurant':[{'id': q.id, 'name':q.name, 'address':q.address, 
                                  'description':q.description, 'price': q.price_range_id, 
                                  'url': q.url, 'phone': q.phone, 'hours':q.hours,
                                  'city':q.city, 'state':q.state, 'country':q.country, 
                                  'zipcode':q.zipcode, 'alcohol': table.type_alcohol, 
                                  'dresscode':q.dress_code_id, 'atmosphere':q.atmosphere_id, 
                                  'urlimg':q.urlimg, 'cuisine': q.cuisine_id, 'parking': q.parking_id, 
                                  'payment': q.payment_id, 'instalation': q.instalation_id }  
                                  for q in query ]}        
          #Cuisine
        elif tablevalue=='8':
            print 'entro a 8'
            table = Cuisine.objects.get(cuisine=dropdowntxt) 
            query = Restaurant.objects.filter(cuisine_id=table.id)
            res = {'restaurant':[{'id': q.id, 'name':q.name, 'address':q.address, 
                                  'description':q.description, 'price': q.price_range_id, 
                                  'url': q.url, 'phone': q.phone, 'hours':q.hours,
                                  'city':q.city, 'state':q.state, 'country':q.country, 
                                  'zipcode':q.zipcode, 'alcohol': q.alcohol_id, 
                                  'dresscode':q.dress_code_id, 'atmosphere':q.atmosphere_id, 
                                  'urlimg':q.urlimg, 'cuisine': table.cuisine, 'parking': q.parking_id, 
                                  'payment': q.payment_id, 'instalation': q.instalation_id } 
                                  for q in query ]}        
        jd=json.dumps(res)
        return HttpResponse(jd, content_type='application/json')
    else:
        rat = Rating.objects.filter(user=u)
        query = Restaurant.objects.all()
        time = datetime.now()
        reviews = Review.objects.all()
        qreviews = reviews.filter(review_time__gte=date.today())[:3]
        random_rest = Rating.objects.filter(rating=5)#[:4]
        rests=[]
        if random_rest:
            for i in random_rest:
                r=Restaurant.objects.get(id=i.id_item_id)
                if r in rests:continue
                rests.append(r)    
        if not rat: 
            msg = "You didn't add any rating. Please vote to get recommendations."
        ratings = Rating.objects.values_list('user','id_item','rating')
        #Depurar la lista para eliminar usuarios repetidos.
        item_list = []
        for i in ratings:
             if i[1] not in item_list:
                 item_list.append(i[1])
        dt = datetime.now()
        pop_item=[]
        for i in item_list:
             item=Restaurant.objects.get(id=i)
             sum=0
             c=0
             t=[]
             for r in ratings:
                 if i == r[1]:
                     c=c+1 
                     sum = sum + float(r[2])
             avg=sum/float(c)
             pop = Popularity (rest = Restaurant.objects.get(id=i) , 
                               users_amount = c, 
                               rating_avg=float(avg), 
                               datet = dt )
             pop.save()

        #Ampliar el rango de rating_avg para obtener mas restaurantes
        #por si son votados con bajo rating.
        popular = Popularity.objects.all().filter(rating_avg=5.0)
        for  p  in popular:
            popit=Restaurant.objects.get(item=p.rest_id)
            if popit in pop_item:continue            
            pop_item.append(popit)
        
        if request.user.is_authenticated():
            u = request.user.profile
        else:
            u='Guest'
        return render_to_response('restaurant/index.html', locals(), 
                                  context_instance=RequestContext(request)) 


def valida_query(dropdowntxt, tablevalue):
       #Precio
        if tablevalue==1:
            print 'entro a 1'
            table = Pricerange.objects.get(type_price=dropdowntxt) 
            query = Restaurant.objects.filter(price_range_id=table.id)
        #instalation
        if tablevalue==2:
            print 'entro a 2'
            table = Instalation.objects.get(type_instalation=dropdowntxt) 
            query = Restaurant.objects.filter(instalation_id=table.id)
        #Parking
        if tablevalue==3:
            print 'entro a 3'
            table = Parking.objects.get(type_parking=dropdowntxt) 
            query = Restaurant.objects.filter(parking_id=table.id) 
        #Atmosphere
        if tablevalue==4:
            print 'entro a 4'
            table = Atmosphere.objects.get(type_atmosphere=dropdowntxt) 
            query = Restaurant.objects.filter(atmosphere_id=table.id)
        #Payment
        if tablevalue==5:
            print 'entro a 5'
            table = Payment.objects.get(type_payment=dropdowntxt)
            query = Restaurant.objects.filter(payment_id=table.id)
        #Dresscode
        if tablevalue==6:
            print 'entro a 6'
            table = Dresscode.objects.get(type_dresscode=dropdowntxt)
            query = Restaurant.objects.filter(dress_code_id=table.id)
        #Alcohol
        if tablevalue==7:
            print 'entro a 7'
            table = Alcohol.objects.get(type_alcohol=dropdowntxt) 
            query = Restaurant.objects.filter(alcohol_id=table.id)
        #Cuisine
        if tablevalue==8:
            print 'entro a 8'
            table = Cuisine.objects.get(type_cuisine=dropdowntxt)
            query = Restaurant.objects.filter(cuisine_id=table.id)
        return query, table

#Creates user profile with context.
def userprofile(request, iduser): 
    u = request.user.profile
    if request.method=='POST':
        form=ProfileForm(request.POST)
        if form.is_valid():
            price = form.cleaned_data['price']
            atribute = form.cleaned_data['atribute']
            cuisine= form.cleaned_data['cuisine']
            u.price_id=price
            u.save()
            #u.location=location
            #u.save()
            u.atribute=atribute
            u.save()
            u.cuisine=cuisine
            u.save()
            form=ProfileForm(request.POST)
            return render_to_response('restaurant/userprofile.html',
                                      locals(), 
                                      context_instance=RequestContext(request)
                                     )
        else:
            metodo = request.method
            form=ProfileForm(request.GET)
            form.errors
            return render_to_response('restaurant/userprofile.html',
                                      locals(), 
                                      context_instance=RequestContext(request)
                                     )
    else:
            form = ProfileForm()
            formuser=UserForm(request.POST)
            metodo = request.method
            return render_to_response('restaurant/userprofile.html',
                                      locals(), 
                                      context_instance=RequestContext(request)
                                     ) 

#Show user profile in template.
def temp_user(request,iduser):
    u = request.user.profile
    user = User.objects.get(id=u.user.id)
    #Todas las reviews del usuario.
    reviews = Review.objects.filter(user_id=u.id)
    #Restaurantes favoritos de usuario
    fav = Rating.objects.filter(user = u.id, rating=5)
    favorites = fav.distinct('id_item')
    fv=[]
    for i in favorites:
        r = Restaurant.objects.get(id=i.id_item.id)
        fv.append(r)
    price=""
    #Prece ranges.
    if(u.price==1):
        price='Very cheap'
    if(u.price==2):
        price='Cheap'
    if(u.price==3):
        price='More and less'
    if(u.price==4):
        price='Expensive'
    if(u.price==5):
        price='Very expensive'
    return render_to_response('restaurant/temp_user.html',
                              locals(),
                              context_instance=RequestContext(request)
                             ) 

#--------------------------------------------
#Final recommendation for users.
#--------------------------------------------
def recommendations_view(request,iduser):    
    u = request.user.profile
    w_avg, g_avg, rExp, pc, pr, sim,  profileVectors, itemsUser, recomend, bc_item, rests, cf_rec = fisIntegrador(request, u.id)
    ppesos = w_avg  #weigthed average.
    pgral = g_avg  #Average.
    recom1 = rExp  #First expert recommendation.
    recom2 = pc #Second recommendation.
    recom3 = pr #Pearson recommendation.
    recom4 = recomend 
    now = datetime.now()
    q = Distance_poi.objects.filter(user=u)
    q.delete()
    restnear=[]
    if rests:
        for i in rests:
            dis = dist_haversine(32.529084, -116.9885298, i.latitude, i.longitude)
            if dis<=2.0 and i not in restnear:
                    restnear.append(i)
                    dp = Distance_poi(user = request.user.profile, 
                                      date=now, 
                                      latitude=i.latitude, 
                                      longitude=i.longitude, 
                                      poi=i, 
                                      dis=dis, 
                                      recom=1)
                    dp.save()
    if bc_item:
        for i in bc_item:
            dis = dist_haversine(32.529084, -116.9885298, i.latitude, i.longitude)
            if dis<=2.0 and i not in restnear:
                restnear.append(i)
                dp = Distance_poi(user = request.user.profile, 
                                  date=now, 
                                  latitude=i.latitude, 
                                  longitude=i.longitude, 
                                  poi=i, 
                                  dis=dis, 
                                  recom=2)
                dp.save()
    if cf_rec:
        for i in cf_rec:
            dis = dist_haversine(32.529084, -116.9885298, i.latitude, i.longitude)
            if dis<=2.0 and i not in restnear:
                    dp = Distance_poi(user = request.user.profile, 
                                      date=now, 
                                      latitude=i.latitude, 
                                      longitude=i.longitude, 
                                      poi=i, 
                                      dis=dis, 
                                      recom=3)
                    dp.save()
                    restnear.append(i)
    q = Distance_poi.objects.filter(user=u)
    return render_to_response('restaurant/recomtest.html',
                              locals(),
                              context_instance=RequestContext(request)
                             )


#Anonymous user recommendations by popularity.
def recomguest(request):
    #-------------------------------------
    # Raings by popularity for each item.
    #-------------------------------------
    ratings = Rating.objects.values_list('user','id_item','rating')
    #Clean duplicated items.
    item_list = []
    for i in ratings:
        if i[1] not in item_list:
            item_list.append(i[1])
    dt = datetime.now()
    avg_list=[]
    for i in item_list:
        item=Restaurant.objects.get(id=i)
        sum=0
        c=0
        t=[]
        for r in ratings:
            if i == r[1]:
                c=c+1 
                sum = sum + float(r[2])
        avg=sum/float(c)
        pop = Popularity (rest = Restaurant.objects.get(id=i) , 
                          users_amount = c, 
                          rating_avg=float(avg), 
                          datet = dt )
        pop.save()
    #avg_list.sort()
    #avg_list.reverse()
    popularity1 = Popularity.objects.all().filter(rating_avg=5)
    #Clean duplicated items.
    items1=[]
    for i in popularity1:
        if i.rest_id not in items1:
            items1.append(i.rest_id)
    #Add rating in the list in case of exists more than one.
    popularity=[]
    for i in items1:
        p=Popularity.objects.filter(rest_id=i, rating_avg=5)
        popularity.append(p[0])
    return render_to_response('restaurant/recomguest.html', 
                              {'popularity':popularity, 
                               'item_list':item_list}
                             )
    
    
#------------------------------------------------
#Weigthed average in the Fuzzy Inference System.
#------------------------------------------------
def fisIntegrador(request, iduser): 
    id=iduser
    #Call Content-Based Algorithm.
    profiles, profiles2, p_it, p_it2, bc_item, hd, lis, val2, sim = vec_profiles(id) 
    profileVectors=profiles2
    itemsUser=profiles
    recomend=hd
    #---------------------------
    # Expert recommendation.
    #---------------------------
    rExp, rests =fisExpert(id)
    #rExp = fisExpert(id)
    predicted=0
    item_rec=0
    for i in rExp:
        if(i[1]>item_rec): #???
            item_rec = i[0]
            predicted = i[1]
    #-----------------------
    # userSimilarity
    #-----------------------
    pc, pr = mat_user(id)
    cf_rec=[]
    for i in pr:
        r=Restaurant.objects.get(id=i[1])
        cf_rec.append(r)
    prp = 0
    c = 0
    promRec = 0
    if(pr):
        if (len(pr)>3):
            for i in range(3):
                prp = prp + pr[i][0]
            promRec = prp/3.0
        else:
            for i in range(len(pr)):
                prp = prp + pr[i][0]
            promRec = prp/float(len(pr))    
        l= []
        for t in pc:
            l.append(t[0])
    
        #Makes positive correlations.
        for c in range(len(l)):
            if(l[c]<0):
                newval = sqrt( l[c]**2 )
                l[c] = newval
    
        #Get similarity average for Fuzzy Inference System.
        sum = 0
        for i in l:
            sum = sum + i        
        averageUser = sum/len(l) 
    else:
        averageUser = 0  #No recommendations.
    #-----------------------
    # Participation.
    #-----------------------
    ratings = Rating.objects.values_list('user','id_item','rating').filter(
                                        interested=0)
    #Clean duplicated items.
    list_u = []
    for i in ratings:
        list_u.append(i[0])
    #list_u.sort()
    u = []
    [(u.append(i)) for i in list_u if i not in u]
    #Dictionary for recommendations.
    p_us = dict([(t[0],{}) for t in ratings])
    for t in ratings:
        p_us[t[0]][t[1]]=float(t[2])
    participation=[]
    #Get user ratings to add them in participations list. 
    #If  user does not exist, does not have ratings.
    for us in u:
        c=0
        t = []
        for r in ratings:
            if(us==r[0]):
                c=c+1
        t.append(us)
        t.append(c)
        #Lista final
        participation.append(t)
    if id in p_us:
        participationUser = len(p_us[id]) 
    else:
        participationUser = 0
    #Error by cold-start problem. 
    resultRecom = 5.0 
    sum=0
    for i in sim:
        sum =sum + i[0]
    if len(sim)==0:
        averageBC=0
    else:
        averageBC = (sum)/float(len(sim))
    #------------------------------------------
    # Promedio de los pesos con el Integrador.
    #------------------------------------------
    exp = experto.eval(averageUser, averageBC, participationUser)
    res = restaurant.eval(averageUser, averageBC, participationUser)
    cor = correlacion.eval(averageUser, averageBC, participationUser)
    #Weigthed Avergae
    w_avg = ((exp * predicted) + (res * resultRecom) + (cor * promRec)) / (exp + res + cor)
    #Average.
    g_avg = (predicted + resultRecom + promRec) / 3.0
    return w_avg, g_avg, rExp, pc, pr, sim,  p_it, itemsUser, recomend, bc_item, rests, cf_rec 

    
#------------------------------------------------------
# CONTENT-BASED ALGORITHM
#------------------------------------------------------
def vec_profiles(id): 
    #---------------------------------
    #Filtering user ratings.
    #---------------------------------
    # Get high ratings: 4.0 or 5.0 score.
    rat2 = Rating.objects.all().filter(user=id,rating=5)
    val2=[]
    if(rat2):       
        [val2.append(i.id_item.id) for i in rat2 if i.id_item.id not in val2]
    #Get user profile.
    profiles=[]
    for i in val2:
        r = Restaurant.objects.get(item=i)
        id_item= r.id
        #4 PRICE RANGES.
        prices = [0,0,0,0]
        for item in range(1,5):
            if(item==int(r.price_range_id)):
                prices[item-1]=1 
        #2 payment
        payment=[0,0]
        for item in range(1,3):
            if(item==int(r.payment_id)):
                payment[item-1]=1  
        #Alcohol 2 types
        alcohol =[0,0]
        for item in range(1,3):
            if(item==int(r.alcohol_id)):
                alcohol[item-1]=1  
        #Smoking T/F 0 y 1
        smoking_area = [0,0]
        if int(r.smoking_area)==1:
            smoking_area[0]=1
        else:
            smoking_area[1]=1
        #3 dress code types
        dress_code=[0,0,0]
        for item in range(1,4):
            if(item==int(r.dress_code_id)):
                dress_code[item-1]=1
        #3 parking type  
        parking =[0,0,0]
        for item in range(1,4):
            if(item==int(r.parking_id)):
                parking[item-1]=1
        #4 instalations
        instalation=[0,0,0,0]
        for item in range(1,5):
            if(item==int(r.instalation_id)):
                instalation[item-1]=1
        #5 atmospheres
        atmosphere=[0,0,0,0,0]
        for item in range(1,6):
            if(item==int(r.atmosphere_id)):
                atmosphere[item-1]=1
        #39 cuisines
        cuisine = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
        for item in range(1,40):
            if(item==int(r.cuisine_id)):
                cuisine[item-1]=1
        #55 ATTRIBUTES    
        profile_item=[]
        profile_item.insert(0,id_item)
        profile_item.insert(1,prices)
        profile_item[1].extend(payment)
        profile_item[1].extend(alcohol)
        profile_item[1].extend(smoking_area)
        profile_item[1].extend(dress_code)
        #profile_item[1].extend(accessibility)
        profile_item[1].extend(parking)
        profile_item[1].extend(instalation)
        profile_item[1].extend(atmosphere)
        profile_item[1].extend(cuisine)
        profiles.append(profile_item)
    #Put in dict items scored by the user.
    p_it = dict([(t[0],{}) for t in profiles])
    for t in profiles:
        p_it[t[0]] = (t[1])
    #Get items.
    rat = Restaurant.objects.all()
    items = []
    [items.append(item) for item in rat if item.id not in val2]
    profiles2=[]
    for r in items:
        id_item = r.id
        #4 price ranges.
        prices = [0,0,0,0]
        for item in range(1,5):
            if(item==int(r.price_range_id)):
                prices[item-1]=1  
        #2 payment
        payment=[0,0]
        for item in range(1,3):
            if(item==int(r.payment_id)):
                payment[item-1]=1  
        #Alcohol 2 types
        alcohol =[0,0]
        for item in range(1,3):
            if(item==int(r.alcohol_id)):
                alcohol[item-1]=1 
        #Smoking T/F 0 y 1
        smoking_area = [0,0]
        if int(r.smoking_area)==1:
            smoking_area[0]=1
        else:
            smoking_area[1]=1
        #3 dress code types
        dress_code=[0,0,0]
        for item in range(1,4):
            if(item==int(r.dress_code_id)):
                dress_code[item-1]=1
        #3 parking type  
        parking =[0,0,0]
        for item in range(1,4):
            if(item==int(r.parking_id)):
                parking[item-1]=1
        #4 instalations
        instalation=[0,0,0,0]
        for item in range(1,5):
            if(item==int(r.instalation_id)):
                instalation[item-1]=1
        #5 atmospheres
        atmosphere=[0,0,0,0,0]
        for item in range(1,6):
            if(item==int(r.atmosphere_id)):
                atmosphere[item-1]=1
        #39 cuisines
        cuisine = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
        for item in range(1,40):
            if(item==int(r.cuisine_id)):
                cuisine[item-1]=1
        #55 ATTRIBUTES    
        profile_item=[]
        profile_item.insert(0,id_item)
        profile_item.insert(1,prices)
        profile_item[1].extend(payment)
        profile_item[1].extend(alcohol)
        profile_item[1].extend(smoking_area)
        profile_item[1].extend(dress_code)
        #profile_item[1].extend(accessibility)
        profile_item[1].extend(parking)
        profile_item[1].extend(instalation)
        profile_item[1].extend(atmosphere)
        profile_item[1].extend(cuisine)
        profiles2.append(profile_item)
    #Get dict to profiles.       
    p_it2 = dict([(t[0],{}) for t in profiles2])
    for t in profiles2:
        p_it2[t[0]] = (t[1])
    #Get Cosine similarity.
    sim_cos = simCosenoItems(p_it, p_it2)
    t=[]
    for i in range(len(sim_cos)):
        tot=len(sim_cos[i])-2
        for j in range(tot):
            if(j<tot):
                if(j%3==0):
                    l_dis=[]
                    l_dis.append(sim_cos[i][j])
                    l_dis.append(sim_cos[i][j+1])
                    l_dis.append(sim_cos[i][j+2])
                    t.append(l_dis)
    #Get items with high correlation.
    #[item_de la lista, item de la base de datos, valor de correlacion]
    hd=[]
    for i in t:
        if i[0]>0.8:
            hd.append(i)
    #Get items in dict.
    #item_user: {item: correlation, etc..}
    lis = dict([(l[0],{}) for l in hd])
    for l in hd:
        lis[l[0]][l[1]] = (l[2])
    #TOP N=3.
    bc_item=[]
    if len(hd):
        for i in range(len(hd)):
            item = Restaurant.objects.get(item=hd[i][1])
            if item in bc_item:continue
            bc_item.append(item)
    return profiles, profiles2, p_it, p_it2, bc_item, hd, lis, val2, sim_cos

#------------------------------------------------
#FIS EXPERT RECOMMENDATIONS.
#------------------------------------------------
def fisExpert(id):
    #Call Content-Based algorithm.
    profiles, profiles2, p_it, p_it2, bc_item, hd, lis, val2, sim = vec_profiles(id) 
    prices=[] 
    it_prices=[] 
    for i in range(len(profiles)):
        for j in range(4):  #size vector de precios.
            if profiles[i][1][j]==1:
                lp =[]
                lp.append(profiles[i][0])#Item
                lp.append(j+1) #Price type
                prices.append(lp) 
                it_prices.append(profiles[i][0])  
    #-------------------
    # Get rating.
    #-------------------
    rtg = Rating.objects.values_list('user','id_item','rating').filter(
                                     interested=0)
    #User ratings.
    val=[]
    for i in rtg:
        if i[1] not in val and i[1] not in val2:
            val.append(i[1])
    #Get Rating average.
    average=[]
    for i in val:
        p_ind=[]
        c=0
        sum=0
        av=0
        for r in rtg: 
            if r[1]==i:
                c = c + 1
                sum = sum + float(r[2])
        if (c<1):continue 
        av=sum/c
        p_ind.append(i)#item.
        p_ind.append(av)#average.
        p_ind.append(c) #amount of users.
        average.append(p_ind)    
    #----------------------------------
    # Get amount of ratings.
    #----------------------------------
    #Get ratings of item.
    votes = []
    for i in val2:
        vo =[]
        c=0
        for r in rtg: 
            if r[1]==i:
                c=c+1
        vo.append(i)
        vo.append(c)
        votes.append(vo) 
    #----------------------------
    # Fusion of lists for FIS.
    #----------------------------
    resProfile = []
    for i in range(len(val)):
        a=0
        b=0
        c=0
        p=[]
        for j in range(len(average)):
            if(average[j][0]==val[i]):
                p.append(val[i])
                p.append(float(average[j][1]))
                a=1
        if(a==0):
            p.append(0.0)
        for k in range(len(prices)):
            if (prices[k][0]==val[i]):
                p.append(prices[k][1])
                b=1
        if(b==0):
            p.append(0.0)
        for m in range(len(votes)):
            if(votes[m][0]==val[i]):
                p.append(float(votes[m][1]))
                c=1
        if(c==0):
            p.append(0.0)
        resProfile.append(p)
    #-----------------------------------
    #Expert FIS.
    #-----------------------------------
    #FIS evaluates averages to define restaurant type(good, bad, excellent).
    #Recommends over the threshold 2.4.
    recomExpert=[]
    rests =[]
    for p in resProfile:
        recom = expert.eval(p[1],p[2],p[3])
        restaurant = Restaurant.objects.get(id=p[0])
        if(recom>3.5): #threshold to add to recommendation list.
            re=[]
            re.append(restaurant)#Add restaurant.
            re.append(recom)#Add prediction.
            recomExpert.append(re)
            rests.append(restaurant)
    recomExpert.sort()
    return recomExpert, rests

#------------------------------------------------------
#COLLABORATIVE FILTERING ALGORITHM.                   |
#------------------------------------------------------
def mat_user(id):   
    r = Rating.objects.values_list('user','id_item','rating')
    list_t=[]
    if(r):
        for i in r:
            list_t.append(i)
    #Dict for recommendations.
    us_it = dict([(t[0],{}) for t in list_t])
    for t in list_t:
        us_it[t[0]][t[1]]=float(t[2])
    uk =us_it.keys()
    #Get recommendations.
    pearsonCorrelation = topMatches(us_it,id)
    pr = getRecommendations(us_it,id,similarity=sim_pearson)
    der = getRecommendations(us_it,id,similarity=sim_distance)
    #TOP N = 3
    l_item=[]  
    if pr:
        if len(pr)>3:
            for i in range(3):
                    item = Restaurant.objects.get(item=pr[i][1])
                    l_item.append(item)#(item.name)
        else:
            for i in range(len(pr)):
                    item = Restaurant.objects.get(item=pr[i][1])
                    l_item.append(item)#(item.name)
    return pearsonCorrelation, pr  

#Restaurant profile.
def view_profile(request,id):
    u = request.user.profile
    r = Restaurant.objects.get(id=id)
    rat = Rating.objects.filter(id_item=id )
    #User Reviews.
    rev = Review.objects.filter(item=id)
    ratavg =Rating.objects.filter(id_item_id=id)
    sum=0
    avg=0
    for i in ratavg:
        sum=sum+i.rating
    if sum>0:
        avg=sum/len(ratavg)
    size=[]
    for i in range(avg):
        size.append('1')
    
    avg2 =(avg*100)/5 
    #Get user ratings
    c1=0
    c2=0
    c3=0
    c4=0
    c5=0
    rts = []
    for i in ratavg:
            print i.rating
            if i.rating==1:
                c1=c1+1
            if i.rating==2:
                c2=c2+1
            if i.rating==3:
                c3=c3+1
            if i.rating==4:
                c4=c4+1
            if i.rating==5:
                c5=c5+1        
    percent1=0
    percent2=0
    percent3=0
    percent4=0
    percent5=0
    if c5>0:
            percent5 =(c5/float(len(ratavg)))*100.0
    if c4>0:
            percent4 =(c4/float(len(ratavg)))*100.0
    if c3>0:
            percent3 =(c3/float(len(ratavg)))*100.0
    if c2>0:
            percent2 =(c2/float(len(ratavg)))*100.0
    if c1>0:
            percent1 =(c1/float(len(ratavg)))*100.0
            
    if request.method=='POST':
        #datajson= json.dumps(json.loads(request.body))
        json_data = json.loads(request.body)
        rating = json_data['dropdownval']['0']['value']
        id_item = Item.objects.get(id=id)
        date = datetime.now()
        u = request.user.profile
        r =Rating(id_item_id=id_item.id, 
                  user = u ,
                  date=date, 
                  rating=rating)
        r.save()
        u = request.user.profile
        r = Restaurant.objects.get(id=id)
        rat = Rating.objects.filter(id_item=id )
        rev = Review.objects.filter(item=id)
        ratavg =Rating.objects.filter(id_item_id=id)
        sum=0.0
        avg=0.0
        for i in ratavg:
            sum=sum+i.rating
        if sum>0:
            avg=sum/len(ratavg)    
        size=[]
        for i in range(int(avg)):
            size.append('1')
        avg2 =(avg*100)/5.0
        c1=0
        c2=0
        c3=0
        c4=0
        c5=0
        for i in ratavg:
                print i.rating
                if i.rating==1:
                    c1=c1+1
                if i.rating==2:
                    c2=c2+1
                if i.rating==3:
                    c3=c3+1
                if i.rating==4:
                    c4=c4+1
                if i.rating==5:
                    c5=c5+1        
        percent1=0
        percent2=0
        percent3=0
        percent4=0
        percent5=0
        if c5>0:
                percent5 =(c5/float(len(ratavg)))*100.0
        if c4>0:
                percent4 =(c4/float(len(ratavg)))*100.0
        if c3>0:
                percent3 =(c3/float(len(ratavg)))*100.0
        if c2>0:
                percent2 =(c2/float(len(ratavg)))*100.0
        if c1>0:
                percent1 =(c1/float(len(ratavg)))*100.0

        return render_to_response('restaurant/view_profile.html', 
                                  locals(), 
                                  context_instance=RequestContext(request)
                                 )
    else:
        return render_to_response ('restaurant/view_profile.html', 
                                   locals(), 
                                   context_instance=RequestContext(request)
                                  ) 
    
#--------------------------------------
#Send reviews to update view_profile.
#--------------------------------------
def addreviewmodal(request, id):
    u = request.user.profile
    restaurant = Restaurant.objects.get(item_id=id)
    item= Item.objects.get(id=id)
    now=datetime.now()
    if request.method=='POST':
        datajson = json.dumps(json.loads(request.body))
        json_data =  json.loads(request.body)
        title = json_data['title']
        good = json_data['good']
        bad = json_data['bad']
        country = json_data['cty']
        rating = json_data['rat']
        #Save review.
        r = Review(item_id=item.id, 
                   restaurant_id=restaurant.id, 
                   user = request.user.profile,  
                   title=title, 
                   good=good, 
                   bad=bad, 
                   review_time=now, 
                   rating=int(rating), 
                   country=country)
        r.save()
        reviews = Review.objects.filter(item_id=item.id)
        rev = {'review':[{'restaurant_id': q.restaurant_id, 
                          'user': str(q.user), 
                          'title': q.title, 
                          'good': q.good, 
                          'bad':q.bad, 
                          'review_time':str(q.review_time), 
                          'rating':q.rating, 
                          'country':q.country }  
                          for q in reviews ]}
        js=json.dumps(rev)
        return HttpResponse(js, content_type='application/json')
    
#----------------------------------------------------
#Get distance between two points.
#----------------------------------------------------
def dist_haversine(lat1,long1,lat2,long2):
    long1,lat1 = (float(long1),float(lat1))
    long2,lat2 = (float(long2),float(lat2))
    geod = pyproj.Geod(ellps="WGS84")
    angle1,angle2,distance = geod.inv(long1, lat1, long2, lat2)
    r = 6371000 #radio terrestre medio, en metros
    c = pi/180 #constante para transformar grados en radianes
    d = 2*r*asin(sqrt(sin(c*(lat2-lat1)/2)**2 + 
                      cos(c*lat1)*cos(c*lat2)*sin(c*(long2-long1)/2)**2))
    dist=(float(d)/1000.00)
    dis=round(dist,2)    
    return dis

#------------------
# User Wishlist.
#------------------
def wishlist(request, iduser):
    u = request.user.profile
    #user = User.objects.get(id=id)
    wlist = Wishlist.objects.filter(user=u, in_wishlist='TRUE')
    lis = []
    for l in wlist:
        r=Restaurant.objects.get(id=l.rest.id)
        #print l.rest.id
        #print r
        lis.append(r)
    return render_to_response('restaurant/wishlist.html', 
                              {'u':u, 'id':id, 'lis':lis}, 
                              context_instance=RequestContext(request)
                             )

#---------------------------
#Insert items in wishlist.
#---------------------------
def addwish(request):
    u = request.user.profile
    now = datetime.now()
    query = Restaurant.objects.all()
    if request.method=='POST':
        u = request.user.profile
        json_data = json.loads(request.body)
        item = int(json_data['iditem'])
        r=Restaurant.objects.get(item_id=item)
        wl=Wishlist.objects.filter(rest_id=item, user=u)
        if wl:
            Wishlist.objects.filter( rest_id=item, user=u).delete()
            #Insert or update wishlist.
        w = Wishlist(rest_id = item, 
                     user= u, 
                     in_wishlist=True)
        w.save()
        msg = {'restaurant':{'item': item }}
        jsd=json.dumps(msg)
    return HttpResponse(jsd, content_type='application/json')

#--------------------------------------------------
#Insert item in wishlist from restaurant profile.
#--------------------------------------------------
def addwish3(request):
    u = request.user.profile
    now = datetime.now()
    query = Restaurant.objects.all()
    if request.method=='POST':   
        #datajson= json.dumps(json.loads(request.body))
        json_data = json.loads(request.body)
        print 'json_data:',json_data
        item = int(json_data['iditem'])
        r=Restaurant.objects.get(item_id=item)
        wl=Wishlist.objects.filter(rest_id=item, user=u)
        if wl:
            Wishlist.objects.filter( rest_id=item, user=u).delete()
        w = Wishlist(rest_id=r.id, user = u, in_wishlist=True)
        w.save()
        msg = {'restaurant':[{'item': item } ]}
        jsd=json.dumps(msg)     
    return HttpResponse(jsd, content_type='application/json')

#-----------------------------
#Delete item from wishlist.
#-----------------------------
def delete_wishlist(request):
    u = request.user.profile
    if request.method == 'POST':
        u = request.user.profile
        #datajson= json.dumps(json.loads(request.body))
        json_data = json.loads(request.body)
        iditem =  json_data['iditem'] 
        r = Restaurant.objects.get(item_id=iditem)
        Wishlist.objects.filter(user=u, rest=r).delete()
        wl=Wishlist.objects.filter(user=u)
        res = {'restaurant':[{'id': q.rest.id, 
                              'name':q.rest.name, 
                              'address':q.rest.address, 
                              'description':q.rest.description, 
                              'price': q.rest.price_range_id, 
                              'url': q.rest.url, 
                              'phone': q.rest.phone, 
                              'hours':q.rest.hours,
                              'city':q.rest.city, 
                              'state':q.rest.state, 
                              'country':q.rest.country, 
                              'zipcode':q.rest.zipcode, 
                              'alcohol': q.rest.alcohol_id, 
                              'dresscode':q.rest.dress_code_id, 
                              'atmosphere':q.rest.atmosphere_id, 
                              'urlimg':q.rest.urlimg, 
                              'cuisine': q.rest.cuisine_id, 
                              'parking': q.rest.parking_id, 
                              'payment': q.rest.payment_id, 
                              'instalation': q.rest.instalation_id }  for q in wl ]}
        jsd=json.dumps(res)
        return HttpResponse(jsd, content_type='application/json')
    return render_to_response('restaurant/wishlist.html', locals()) 

#------------------------------
#Delete all items of wishlist.
#------------------------------
def delete_all(request):
    u = request.user.profile
    Wishlist.objects.filter(user=u).delete()
    return render_to_response('restaurant/wishlist.html',  
                              locals(), 
                              context_instance=RequestContext(request)) 

#--------------------------------
#Contextualized recommendations.
#--------------------------------
def recomtest(request):
    u = request.user.profile
    q = Distance_poi.objects.filter(user=u)
    q.delete()
    rat = Rating.objects.filter(user=u) 
    print 'rat', rat
    if rat:   
        w_avg, g_avg, rExp, pc, pr, sim,  profileVectors, itemsUser, recomend, bc_item, rests, cf_rec = fisIntegrador(request, u.id)
        #Insert with post method.
        if request.method=='POST':
            print 'entro a post'
            u = request.user.profile
            q = Distance_poi.objects.filter(user=u)
            q.delete()
            #datajson= json.dumps(json.loads(request.body))
            json_data = json.loads(request.body)
            value = json_data['tableval']['0']['value']
            print json_data
            print u.latitude, u.longitude
            now=datetime.now()
            print now
            restnear=[]
            if rests:
                    for i in rests:
                        if not u.latitude and not u.longitude:continue
                        dis = dist_haversine(float(u.latitude),
                                             float( u.longitude), 
                                             float(i.latitude), 
                                             float(i.longitude)
                                            )
                        if dis<=2.0 and i not in restnear:
                                restnear.append(i)
                                #Se puede optimizar utilizando listas.
                                dp = Distance_poi(user = request.user.profile, 
                                                  date=now, latitude=i.latitude, 
                                                  longitude=i.longitude, 
                                                  poi=i, 
                                                  dis=dis, 
                                                  recom=1)
                                dp.save()
            if bc_item:
                    print bc_item[0]
                    for i in bc_item:
                        if not u.latitude and not u.longitude:continue
                        dis = dist_haversine(u.latitude, 
                                             u.longitude, 
                                             i.latitude, 
                                             i.longitude)
                        if dis<=2.0 and i not in restnear:
                            restnear.append(i)
                            dp = Distance_poi(user = request.user.profile, 
                                              date=now, 
                                              latitude=i.latitude, 
                                              longitude=i.longitude, 
                                              poi=i, 
                                              dis=dis, 
                                              recom=2)
                            dp.save()
            if cf_rec:
                    for i in cf_rec:
                        if not u.latitude and not u.longitude:continue
                        dis = dist_haversine(u.latitude, 
                                             u.longitude, 
                                             i.latitude, 
                                             i.longitude)
                        if dis<=2.0 and i not in restnear:
                                dp = Distance_poi(user = request.user.profile, 
                                                  date=now, 
                                                  latitude=i.latitude, 
                                                  longitude=i.longitude, 
                                                  poi=i, 
                                                  dis=dis, 
                                                  recom=3)
                                dp.save()
                                restnear.append(i)
            if value=='1': 
                        jd=rests
                        res = {'restaurant':[{'id': q.id, 'name':q.name, 'address':q.address, 
                                              'description':q.description, 'price': q.price_range_id, 
                                              'url': q.url, 'phone': q.phone, 'hours':q.hours,
                                              'city':q.city, 'state':q.state, 'country':q.country, 
                                              'zipcode':q.zipcode, 'alcohol': q.alcohol_id, 
                                              'dresscode':q.dress_code_id, 'atmosphere':q.atmosphere_id, 
                                              'urlimg':q.urlimg, 'cuisine': q.cuisine_id, 'parking': q.parking_id, 
                                              'payment': q.payment_id, 'instalation': q.instalation_id, 
                                              'value': str(value) }  for q in jd ]}
                        jsd=json.dumps(res)
            if value=='2':
                        jd=bc_item
                        res = {'restaurant':[{'id': q.id, 'name':q.name, 'address':q.address, 
                                              'description':q.description, 'price': q.price_range_id, 
                                              'url': q.url, 'phone': q.phone, 'hours':q.hours,
                                              'city':q.city, 'state':q.state, 'country':q.country, 
                                              'zipcode':q.zipcode, 'alcohol': q.alcohol_id, 
                                              'dresscode':q.dress_code_id, 'atmosphere':q.atmosphere_id, 
                                              'urlimg':q.urlimg, 'cuisine': q.cuisine_id, 'parking': q.parking_id, 
                                              'payment': q.payment_id, 'instalation': q.instalation_id, 
                                              'value': str(value) }  for q in jd ]}
                        jsd=json.dumps(res)
            if value=='3':
                        jd=cf_rec
                        res = {'restaurant':[{'id': q.id, 'name':q.name, 'address':q.address, 
                                              'description':q.description, 'price': q.price_range_id, 
                                              'url': q.url, 'phone': q.phone, 'hours':q.hours,
                                              'city':q.city, 'state':q.state, 'country':q.country, 
                                              'zipcode':q.zipcode, 'alcohol': q.alcohol_id, 
                                              'dresscode':q.dress_code_id, 'atmosphere':q.atmosphere_id, 
                                              'urlimg':q.urlimg, 'cuisine': q.cuisine_id, 'parking': q.parking_id, 
                                              'payment': q.payment_id, 'instalation': q.instalation_id, 
                                              'value': str(value) }  for q in jd ]}
                        jsd=json.dumps(res)
            if value=='4':
                        jd=Distance_poi.objects.filter(user=u)
                        if u.latitude:
                            res = {'restaurant':[{'user_id': q.user_id, 'date':str(q.date), 'poi_id': q.poi_id, 
                                                  'dis': str(q.dis), 'recom': q.recom, 'address':q.poi.address, 
                                                  'description':q.poi.description, 'price': q.poi.price_range_id, 
                                                  'url': q.poi.url, 'phone': q.poi.phone, 'hours':q.poi.hours, 
                                                  'name':q.poi.name,'city':q.poi.city, 'state':q.poi.state, 
                                                  'country':q.poi.country, 'zipcode':q.poi.zipcode, 
                                                  'alcohol': q.poi.alcohol_id, 'dresscode':q.poi.dress_code_id, 
                                                  'atmosphere':q.poi.atmosphere_id, 'urlimg':q.poi.urlimg, 
                                                  'cuisine': q.poi.cuisine_id, 'parking': q.poi.parking_id, 
                                                  'payment': q.poi.payment_id, 'instalation': q.poi.instalation_id, 
                                                  'value': str(value) }  for q in jd ]}
                        else:
                            res = {'restaurant':[{'msj':'You do not have any location.'}]}
                        jsd=json.dumps(res)
            return HttpResponse(jsd, content_type='application/json')
    else: 
        msg = "You didn't add any rating. Please vote to get recommendations."
            
    return render_to_response('restaurant/recomtest.html',
                              locals(), 
                              context_instance=RequestContext(request)
                             )

#------------------------------------------
#Get user location(latitude, longitude).
#------------------------------------------
def currentlocation(request):
    #Save location.
    if request.method=='POST':   
        #datajson= json.dumps(json.loads(request.body))
        json_data = json.loads(request.body)
        latitude = json_data['latitude']
        longitude = json_data['longitude']
        u = request.user.profile
        now = datetime.now()      
        #Adjust context.
        c = CurrentLocation.objects.filter(user=u)
        if c: 
            for i in c: #'I'=Inactive.
                i.status='I'
        #Update user location in user profile.
        u.latitude = latitude
        u.longitude = longitude
        u.save()
        #Save current location.
        cp = CurrentLocation(user=u, 
                             latitude=latitude, 
                             longitude=longitude, 
                             date=now, 
                             status='A')
        cp.save()
        msg="Saved data."
    return HttpResponse(msg, content_type='application/json')

def addRatingIndex(request):
    u = request.user.profile
    date = datetime.now()
    query = Restaurant.objects.all()
    print 'entrara a post'
    if request.method=='POST':   
        #datajson= json.dumps(json.loads(request.body))
        json_data = json.loads(request.body)
        print 'json_data:',json_data
        item = int(json_data['iditem'])
        r=Restaurant.objects.get(item_id=item)
        rat =Rating(id_item_id=item, user = u , date=date, rating=5)
        rat.save()
        msg = {'restaurant':[{'item': item } ]}
        jsd=json.dumps(msg)
    return HttpResponse(jsd, content_type='application/json')

#---------------------------
# If review is helpful.
#---------------------------
def isHelpful(request):
    u = request.user.profile
    date = datetime.now()
    query = Restaurant.objects.all()
    if request.method=='POST':   
        #datajson= json.dumps(json.loads(request.body))
        json_data = json.loads(request.body)
        print 'json_data:',json_data
        item = int(json_data['iditem'])
        r=Review.objects.get(id=item)
        rest = Restaurant.objects.get(item_id=r.restaurant)
        r.is_helpful=True
        r.save()
        r.helpful=r.helpful+1
        r.save()
        msg = {'restaurant':{'item': item, 'rest':rest.item_id }}
        jsd=json.dumps(msg)
    return HttpResponse(jsd, content_type='application/json')

#---------------------
#Get popular items.
#---------------------
def topten(request):
    #-----------------------
    # Reviews of all users.
    #-----------------------
    u = request.user.profile
    rev = Review.objects.order_by('-rating')    
    allusers = User.objects.all()
    if request.method=='POST':   
        #datajson= json.dumps(json.loads(request.body))
        json_data = json.loads(request.body)
        iduser = int(json_data['iduser']['0']['value'])
        user =User.objects.get(id=iduser)    
        rev = Review.objects.filter(user_id=iduser)
        res = {'review':[{'user': r.user_id.user, 
                          'review_time':str(r.review_time), 
                          'restaurant': r.restaurant_id.restaurant, 
                          'title': r.title, 
                          'good': r.good, 
                          'bad':r.bad }  for r in rev ]}
        jsd=json.dumps(res)
        return HttpResponse(jsd, content_type='application/json')
    else:
        return render_to_response('restaurant/topten.html', 
                                  locals(), 
                                  context_instance=RequestContext(request)
                                 ) 
    
