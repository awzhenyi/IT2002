from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from .models import *

# Create your views here.
def index(request):
    return render(request, 'AppORM/index.html')

def result(request):
    ##Get search string sent from the from
    search_string = request.GET.get('name','')
    ##Use ORM instead of raw query
    results = Item.objects.filter(i_name__regex=r'%s'%(search_string))
    
    results = [(r.i_id,r.i_im_id,r.i_name,r.i_price) for r in results]

    result_dict = {'records':results}

    return render(request, 'AppORM/result.html', result_dict)

def query(request):
    query = """SELECT w.w_country, SUM(s.s_qty)
            FROM warehouse w, stock s, item i
            WHERE w.w_id = s.w_id AND i.i_id = s.i_id
            AND i.i_name = 'Aspirin'
            GROUP BY w.w_country; """
    c = connection.cursor()
    c.execute(query)
    results = c.fetchall()
    return JsonResponse(results, safe=False)

def report(query):
    return render(query, 'AppORM/report.html')

