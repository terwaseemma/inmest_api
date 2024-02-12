from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View

# Create your views here.
def say_hello(req):
    return HttpResponse("<h1>Hello Fred</h1>")

def user_profile(request):
    return JsonResponse(
        {"name": "Emmanuel", 
        "email": "emmanuelterwase1@gmail.com", 
        "phone_number": "+2349037947684"
        })

def filter_queries(request, query_id):
    response_data = {
        'id': query_id,
        'title': 'Permission',
        'description': 'Going to Accra',
        'status': "Approved",
        'submitted_by': 'Emmanuel'
    }
    return JsonResponse(response_data)
    

class QueryView(View):
        queries =[
            { "id":1, "title": "Going home"},
            { "id":2, "title": "Going to nile"},
            { "id":3, "title": "Going to church"}   
            ]
        def get(self, req):

            return JsonResponse({"result": self.queries})

        def post(self, request):

            return ({"status ": "Ok"})