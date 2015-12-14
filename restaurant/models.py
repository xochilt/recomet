# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User #Modelo de usuario de Django
import datetime

#Para geo-position------------------------------
from django.db import models
from geoposition.fields import GeopositionField

from django.db import models
from django.forms import ModelForm, TextInput, widgets
from django import forms
from django.core.validators import MaxLengthValidator

from django_countries.fields import CountryField

LANG = (
    ('es', 'Espanol'),
    ('en', 'English'),
    ('fr', 'French'),
    ('jp', 'Japanese'),
   )

COUNTRY = (
    ('mx', 'Mexico'),
    ('us', 'U.S.A.'),
    ('fr', 'France'),
    ('sp', 'Spain'),
    ('cn', 'Canada'),
    ('gt', 'Guatemala'),
    ('ch', 'China'),
    ('me', 'Middle East'),
   )

RATING = (
    (5, 'Woow, awesome!'),
    (4, 'Yes, I love it!'),
    (3, 'Normal, Ok.'),
    (2, 'Well,I have had better experiences.'),
    (1, 'Hu, no thanks.'),
   )


class Cuisine(models.Model):
    cuisine = models.CharField(max_length=28)
    def __unicode__(self):
        return self.cuisine

class Atribute_Group(models.Model):
    group = models.CharField(max_length=32, null=True)
    def __unicode__(self):
        return self.group

class Atribute(models.Model):
    atribute = models.CharField(max_length=32)
    group = models.ForeignKey(Atribute_Group) 
    def __unicode__(self):
        return self.atribute
    
class RestaurantChain(models.Model):
    is_international = models.BooleanField()
    name = models.CharField(max_length=128)
    speciality = models.CharField(max_length=128)
    year_founded = models.PositiveSmallIntegerField(null=True)
    locations_worldwide = models.PositiveSmallIntegerField(null=True)
    
    def __unicode__(self):
        return self.name
    
class Recommender_rule(models.Model):
    rule = models.CharField(max_length=500, null=True)
    def __unicode__(self):
        return self.rule
    
class Item(models.Model):
    rule = models.ForeignKey(Recommender_rule, null=True)
    def __unicode__(self):
        return self.rule.rule

#-----------------------------
#CATALOGOS PARA RESTAURANTE
#-----------------------------
class Alcohol(models.Model):
    type_alcohol = models.CharField(max_length=100, null=True) 
    def __unicode__(self):
        return self.type_alcohol

#No se considera en el modelo de contexto.
class Area(models.Model):
    type_area = models.CharField(max_length=100, null=True) 
    def __unicode__(self):
        return self.type_area

class Atmosphere(models.Model):
    type_atmosphere = models.CharField(max_length=100, null=True) 
    def __unicode__(self):
        return self.type_atmosphere

class Dresscode(models.Model):
    type_dresscode = models.CharField(max_length=100, null=True) 
    def __unicode__(self):
        return self.type_dresscode

class Pricerange(models.Model):
    type_price = models.CharField(max_length=100, null=True) 
    def __unicode__(self):
        return self.type_price

class Parking(models.Model):
    type_parking = models.CharField(max_length=100, null=True) 
    def __unicode__(self):
        return self.type_parking
    
class Payment(models.Model):
    type_payment = models.CharField(max_length=100, null=True) 
    def __unicode__(self):
        return self.type_payment
    
class Instalation(models.Model):
    type_instalation = models.CharField(max_length=100, null=True) 
    def __unicode__(self):
        return self.type_instalation


class Restaurant(models.Model):
    item = models.OneToOneField(Item, unique=True) #Llave primaria
    name = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=1000, null=True)
    description = models.CharField(max_length=6000, null=True)
    needs_reservation = models.BooleanField(default=False)
    price_range = models.ForeignKey(Pricerange, null=True)
    url = models.CharField(max_length=1000, null=True)
    phone = models.CharField(max_length=18, null=True)
    hours = models.CharField(max_length=50, null=True)
    slug_name = models.SlugField(max_length=18, null=True)
    chain = models.ForeignKey(RestaurantChain, null=True)
    pub_date =  models.DateTimeField(default=datetime.datetime.now)
    #Campos agregados para usar un solo modelo de restaurante.
    latitude = models.DecimalField(max_digits=8, decimal_places=5, null=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=5, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    fax = models.CharField(max_length=20, null=True)
    zipcode = models.CharField(max_length=20, null=True)
    #Para perfil
    alcohol = models.ForeignKey(Alcohol, null=True)
    smoking_area = models.CharField(max_length=2, null=True)
    dress_code = models.ForeignKey(Dresscode, null=True)
    atmosphere = models.ForeignKey(Atmosphere, null=True)
    parking = models.ForeignKey(Parking, null=True)
    payment = models.ForeignKey(Payment, null=True)
    instalation = models.ForeignKey(Instalation, null=True)
    cuisine =  models.ForeignKey(Cuisine, null=True)
    urlimg = models.CharField(max_length=3000, null=True)
    
    #Agregados
    atribute = models.ManyToManyField(Atribute)
    #cuisine = models.ManyToManyField(Cuisine)
    def __unicode__(self):
        return self.name

class Container(models.Model):
    container_name = models.CharField(max_length=64) 
    is_public = models.BooleanField()
    def __unicode__(self):
        return self.container_name

class Rating_Dimension(models.Model):
    dimension_name = models.CharField(max_length=64)
    priority = models.IntegerField(null=True)
    
    def __unicode__(self):
        return self.dimension_name
    
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    #Add fields.
    first_name = models.CharField(max_length=100, null=True) 
    last_name = models.CharField(max_length=100, null=True) 
    address = models.CharField(max_length=500, null=True) 
    price = models.ForeignKey(Pricerange, null=True)
    location = models.CharField(max_length=500, null=True)
    latitude = models.DecimalField(max_digits=8, decimal_places=5, null=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=5, null=True)   
    atribute = models.ManyToManyField(Atribute)
    cuisine = models.ManyToManyField(Cuisine)
    #Relations 
    container = models.ManyToManyField(Container, through='Container_User')
    ratings = models.ManyToManyField(Item, through='Rating', related_name='ratings')
    reviews = models.ManyToManyField(Item, through='Review', related_name='reviews')
    def __unicode__(self):
        return self.user.username


class Rating(models.Model):
    id_item =  models.ForeignKey(Item) 
    user = models.ForeignKey(UserProfile)
    id_dimension = models.ForeignKey(Rating_Dimension, null=True)
    date = models.DateTimeField()
    rating = models.IntegerField(choices=RATING)
    interested = models.BooleanField(default=False)
    def __unicode__(self):
        return self.user.user.username  #Cambie por username first_name

#Remodelado de Rating por el error de userprofile_id.

class Opinionreview(models.Model):
    opinion =  models.CharField(max_length=50, null=True)
    def __unicode__(self):
        return self.opinion

#Funciona con relacion M2M de userprofile. 
class Review(models.Model):
    item = models.ForeignKey(Item)
    restaurant = models.ForeignKey(Restaurant)
    user = models.ForeignKey(UserProfile) #id_user
    title = models.CharField(max_length=128,  null=True)
    good = models.TextField(validators=[MaxLengthValidator(200)], null=True)
    bad = models.TextField(validators=[MaxLengthValidator(200)], null=True)
    status = models.PositiveSmallIntegerField(null=True)
    review_time = models.DateTimeField()
    #review_time = datetime.datetime.now()
    is_helpful = models.BooleanField(default=False)
    helpful = models.IntegerField(max_length=10, null=True, default=0)
    language = models.CharField(max_length=2, choices=LANG, null=True)
    rating = models.IntegerField(max_length=10, null=True) #models.ForeignKey(Opinionreview)
    country = models.CharField(max_length=20, null=True) #CountryField(blank_label='(select country)')
    
    def __unicode__(self):
        return self.title  
    
class Friends(models.Model):
    user = models.ForeignKey(User, related_name='id_user')
    id_friend = models.ForeignKey(User, related_name='friends') 
    time_added = models.DateTimeField(null=True)
    
    def __unicode__(self):
        return self.user.user.first_name

class Container_User(models.Model):
    id_container =  models.ForeignKey(Container)  
    user = models.ForeignKey(UserProfile)
    id_itemid_item = models.ForeignKey(Item)
    
    def __unicode__(self):
       return self.user.user.first_name
    

class Tag(models.Model):
    tag = models.CharField(max_length=18)
    id_item = models.ForeignKey(Item) 
    
    def __unicode__(self):
        return self.tag
    
class Wishlist(models.Model):
    rest =  models.ForeignKey(Restaurant)  
    user = models.ForeignKey(UserProfile)
    in_wishlist = models.BooleanField(default=False)

class Popularity(models.Model):
    rest =  models.ForeignKey(Restaurant)  
    users_amount = models.IntegerField(null=True)
    rating_avg = models.IntegerField(null=True)
    datet = models.DateTimeField(default=datetime.datetime.now)


#TABLA PARA GUARDAR LA POSICION ACTUAL DEL USUARIO.
class CurrentLocation(models.Model):
    user =  models.ForeignKey(UserProfile)  
    latitude = models.DecimalField(max_digits=8, decimal_places=5, null=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=5, null=True)
    date = models.DateTimeField(default=datetime.datetime.now)
    status = models.CharField(max_length=10)
    def __unicode__(self):
        return self.user

#TABLAS PARA PUNTOS DE INTERES DEL USUARIO. SE UTILIZAN PARA LAS
#RECOMENDACIONES NEARBY.
#copy activitytree_itmovies from 'itmovie.csv' delimiters ',' CSV;
##MODELO PARA OBTENER LA DISTANCIA DESDE LA UBICACION ACTUAL DEL USUARIO
##HASTA EL PUNTO DE INTERES DEL USUARIO ACTUAL CON RESTAURANTES NO GEOPLACES.
#
class Distance_poi(models.Model):
    user = models.ForeignKey(UserProfile)
    date = models.DateTimeField(default=datetime.datetime.now)
    latitude = models.DecimalField(max_digits=8, decimal_places=5, null=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=5, null=True)
    poi = models.ForeignKey(Restaurant) #restaurant de la base de datos
    dis = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    recom =  models.IntegerField(null=True)
    
    
class Distancia(models.Model):
    user = models.ForeignKey(UserProfile)
    #user = request.user.get_profile()
    date = models.DateTimeField()
    location = models.CharField(max_length=200, null=True)
    #latitude = models.DecimalField(max_digits=8, decimal_places=5, null=True)
    #longitude = models.DecimalField(max_digits=8, decimal_places=5, null=True)
    poi = models.ForeignKey(Restaurant) #restaurant de la base de datos
    

class PointOfInterest(models.Model):
    name = models.CharField(max_length=100)
    position = GeopositionField()
   
    class Meta:
        verbose_name_plural = 'points of interest'
#

   
#copy restaurant_restaurant from 'restaurantes1.csv' delimiters ',' CSV;
#Para USERPROFILE DEPRECATED---------------------------------------------------
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


