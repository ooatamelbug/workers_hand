from django.contrib import admin
from .models import Category, City, Workers, Home, RateWorkers, Phone, Governorate

# Register your models here.

admin.site.register(Category)
admin.site.register(City)
admin.site.register(Workers)
admin.site.register(Home)
admin.site.register(RateWorkers)
admin.site.register(Phone)
admin.site.register(Governorate)


