from django.contrib import admin
from Carpool.models import *
#Register your models here.
admin.site.register(Drivers)
admin.site.register(Riders)
admin.site.register(Users)
admin.site.register(Time)
admin.site.register(Locations)
admin.site.register(Driverrequests)
admin.site.register(Riderrequests)