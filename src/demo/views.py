from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def index(request):
    print('Index called',request.POST)
    raise Exception("Exception from the view")
    return JsonResponse({"Message":"Hello, World!"})