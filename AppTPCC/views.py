from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'AppTPCC/index.html')

def result(request):
    ##Get search string sent from the from
    search_string = request.GET.get('name','')
    ##Query
    query = 'SELECT * FROM item WHERE i_name ~ \'%s\'' %(search_string)
    ##The connection object
    c = connection.cursor()

    ##Execute Query
    c.execute(query)
    #Fetch all the rows. fetchall() returns a list of tuples
    results = c.fetchall()
    result_dict = {'records':results}
    return render(request, 'AppTPCC/result.html', result_dict)

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

def test(request):
    query = """SELECT w.w_id, (CASE WHEN s.s_qty IS NULL THEN 0 ELSE s.s_qty END)
	    FROM stock s INNER JOIN item i ON s.i_id = i.i_id and i.i_name = 'Aspirin'
	    RIGHT OUTER JOIN warehouse w ON s.w_id = w.w_id
	    GROUP BY w.w_id, s.s_qty
	    ORDER BY s.s_qty DESC NULLS LAST;"""

    c = connection.cursor()
    c.execute(query)
    results = c.fetchall()
    return JsonResponse(results, safe=False)

def visualise(test):
    return render(test, 'AppTPCC/visualise.html')

def report(query):
    return render(query, 'AppTPCC/report.html')
