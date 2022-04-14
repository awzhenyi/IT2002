from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from Carpool.models import Users, Riders, Driverrequests, Riderrequests

class RequestForm(ModelForm):
	class Meta:
		model = Driverrequests
		fields = '__all__'

class RiderRequestForm(ModelForm):
	class Meta:
		model = Riderrequests
		fields = '__all__'