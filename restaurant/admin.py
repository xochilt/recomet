from django.contrib import admin

#!/usr/bin/env python
from restaurant.models import Container, Rating, Item, Container_User, Review, UserProfile, Restaurant, RestaurantChain, PointOfInterest
from django.contrib import admin


class PointOfInterestAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'position_map',)

    def position_map(self, instance):
        if instance.position is not None:
            return '<img src="http://maps.googleapis.com/maps/api/staticmap?center=%(latitude)s,%(longitude)s&zoom=%(zoom)s&size=%(width)sx%(height)s&maptype=roadmap&markers=%(latitude)s,%(longitude)s&sensor=false&visual_refresh=true&scale=%(scale)s" width="%(width)s" height="%(height)s">' % {
                'latitude': instance.position.latitude,
                'longitude': instance.position.longitude,
                'zoom': 15,
                'width': 100,
                'height': 100,
                'scale': 2
            }
    position_map.allow_tags = True


admin.site.register(PointOfInterest, PointOfInterestAdmin)


class RestaurantInline(admin.TabularInline):
    model = Restaurant
    extra = 3

    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
        was_published_today.short_description = 'Published today?'
        
admin.site.register(Restaurant)

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 3

    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
        was_published_today.short_description = 'Published today?'

admin.site.register(Review)

class Container_UserInline(admin.TabularInline):
    model = Container_User
    extra = 3

    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
        was_published_today.short_description = 'Published today?'

admin.site.register(Container_User)

class ItemInline(admin.TabularInline):
    model = Item
    extra = 3

    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
        was_published_today.short_description = 'Published today?'
        
admin.site.register(Item)

class UserProfileInline(admin.TabularInline):
    model = UserProfile
    extra = 1

    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
        was_published_today.short_description = 'Published today?'
        
admin.site.register(UserProfile)

class RatingInline(admin.TabularInline):
    model = Rating
    extra = 5

    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
        was_published_today.short_description = 'Published today?'
        
admin.site.register(Rating)


class RestAdmin(admin.ModelAdmin):
    
    #- RESTAURANT -------------------------------------------------
    fieldsets = [
    ('Date information',    {'fields': ['name']}),
    (None,                  {'fields': ['id_restaurant']}),
    (None,                  {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [RestaurantInline]
    list_display = ('name','was_published_today', 'pub_date')
    
    #- REVIEW --------------------------------------------------------
    fieldsets = [
    (None,                  {'fields': ['id_user']}),
    ]
    inlines = [ReviewInline]
    list_display = ('id_user','was_published_today')
    
    #- CONTAINER -----------------------------------------------------------
    fieldsets = [
    ('Date information',    {'fields': ['id_user']}),
    (None,                  {'fields': ['id_container']}),
    ]
    inlines = [Container_UserInline]
    list_display = ('id_user','id_container','was_published_today')
    
    #- ITEM -----------------------------------------------------------
    fieldsets = [
    ('Date information',    {'fields': ['id_item']}),
    (None,                  {'fields': ['id_recommender_rule']}),
    (None,                  {'fields': ['item_name']}),
    ]
    inlines = [ItemInline]
    list_display = ('id_item','id_recommender_rule','item_name','was_published_today')

    #- PROFILE -----------------------------------------------------------
    fieldsets = [
    ('Date information',    {'fields': ['username']}),
    (None,                  {'fields': ['firs_name']}),
    ]
    inlines = [UserProfileInline]
    list_display = ('username','first_name','was_published_today')
    
    #- RATING -----------------------------------------------------------
    fieldsets = [
    ('Date information',    {'fields': ['id_user']}),
    (None,                  {'fields': ['id_item']}),
    ]
    inlines = [RatingInline]
    list_display = ('id_user','id_item','was_published_today')
    
admin.site.register( [RestaurantChain, ])

