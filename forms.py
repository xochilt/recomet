#!/usr/bin/env python
from django.forms import ModelForm
from restaurant.models import UserProfile, Restaurant, 
                            Rating, Review, Pricerange
from django import forms
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


class UserForm(ModelForm): 
    #Para completar el perfil.
    class Meta:
        model=User
        fields  = ('first_name', 'last_name')

    def __unicode__(self):
        return self.user
    
    
class ProfileForm(ModelForm): 
    #Para completar el perfil.
    class Meta:
        model=UserProfile
        exclude = ('latitude', 'longitude','user','container', 
                   'reviews', 'ratings', 'first_name', 'last_name', 
                   'address', 'location')

    def __unicode__(self):
        return self.user
    

class RestForm(ModelForm):

    class Meta:
        model=Restaurant
        
    def __unicode__(self):
        return self.name


class RatingForm(ModelForm):
    class Meta:
        model = Rating
        exclude = ('id_item', 'user', 'date', 
                   'id_dimension', 'interested')
        
    def __unicode__(self):
        return self.user.user.first_name
    
    
class DistForm(forms.Form):
    poi = forms.ModelChoiceField(
        queryset=Restaurant.objects.all().order_by('name'))


class ReviewForm(ModelForm):
    
    class Meta:
        model = Review
        fields = ('title', 'good', 'bad', 'rating','country')
        widgets = {'country': CountrySelectWidget()} 
    def __unicode__(self):
        return self.title

    
class PriceForm(forms.Form):
    price = forms.ModelChoiceField(
        queryset=Pricerange.objects.all().order_by('id'))

