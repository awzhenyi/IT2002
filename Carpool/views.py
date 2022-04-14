from django.shortcuts import render, redirect
from Carpool.models import Users, Drivers, Riders, Driverrequests
from django.contrib.auth.models import auth
from .forms import RequestForm, RiderRequestForm
from django.contrib.auth import login, authenticate
from django.db import connection, transaction
from django.http import HttpResponse
from django.contrib import messages

#Create your views here.
def register(request):
	if request.method == "POST":
		username = request.POST.get('username','')
		password = request.POST.get('password','')
		email_address = request.POST.get('email_address','')
		fname = request.POST.get('first_name','')
		lname = request.POST.get('last_name','')
		Users(username = username, password=password,email_address=email_address,first_name=fname,last_name=lname).save()
		return redirect('Carpool/success.html')
	return render(request,'Carpool/register.html')

def login(request):
	if request.method == "POST":
		username = request.POST.get('username','')
		password = request.POST.get('password','')
		query = """SELECT * FROM Users WHERE username = %s AND password = %s"""
		c = connection.cursor()
		c.execute(query, [username,password])
		connection.commit()
		results = c.fetchone()
		if results == None:
			messages.error(request,"You have entered invalid credentials!")
			return render(request,'Carpool/login.html')
		else:
			request.session['username'] = username
			return redirect('Carpool/index.html')
	return render(request, 'Carpool/login.html')

def logout(request):
	request.session.clear()
	return render(request,'Carpool/logout.html')

def DriverAddRequest(request):
	if request.session.has_key:
		form = RequestForm()
		if request.method == "POST":
			form = RequestForm(request.POST)
			if form.is_valid():
				form.save()
		context = {'form':form}
		return render(request, 'Carpool/DriverAddRequest.html',context)
	else:
		return redirect('Carpool/login.html')

def RiderAddRequest(request):
	form = RiderRequestForm()
	if request.method == "POST":
		form = RiderRequestForm(request.POST)
		if form.is_valid():
			form.save()
	context = {'form':form}
	return render(request, 'Carpool/RiderAddRequest.html',context)

def temp(request,pk):
	ride = Driverrequests.objects.get(username=pk)
	form = RequestForm(instance=ride)
	Driverrequests.objects.get(username=pk).delete()
	if request.method == "POST":
		form = RequestForm(request.POST,instance=ride)
		form.save()
	context = {'form':form}
	return render(request, 'Carpool/temp.html',context)

def home(request):
	return render(request, 'Carpool/home.html')

def confirm(request):
	return render(request, 'Carpool/confirm.html')
def success(request):
	return render(request, 'Carpool/success.html')

def index(request):
    return render(request, 'Carpool/index.html')

def home(request):
    return render(request, 'Carpool/home.html')

def result(request):
	search_string = request.GET.get('from','')
	search_string1 = request.GET.get('to','')
	search_string2 = request.GET.get('time','')
	query = """SELECT * FROM Driverrequests WHERE from_location = %s AND to_location = %s AND timeslot = %s AND rider_firstname ISNULL"""
	c = connection.cursor()
	c.execute(query, [search_string,search_string1,search_string2])
	results = c.fetchall()
	result_dict = {'records':results}
	return render(request, 'Carpool/Results.html', result_dict)
		

