from typing import Any
from django.http import JsonResponse


# Function based Middleware

def set_request_data(get_response):
    print("set_request_data middleware")
    def wrapper(request):
        print(f"post data = {request.POST}")
        data = request.POST.get('number')
        print(data)
        request.POST = {"data":data}
        print("Start")
        response = get_response(request)
        print("End")
        return response
    return wrapper

def check_even(response):
    print("-->")
    def wrapper(request):
        print("start-->")
        number = request.POST.get("number")
        if number and int(number) % 2:
            return JsonResponse({"message":"The given number is even"})
        respons = response(request)
        print("End-->")
        return respons
    return wrapper

# ----------------- E N D ---------------------------------------------

# Function based middleware

class SetRequestData:
    def __init__(self,get_response):
        print("Initialized")
        self.get_response = get_response

    def __call__(self, request):
        print("post data",request.POST)
        data = request.POST.get('number')
        print(data)
        print("Start")
        response = self.get_response(request)
        print("End")
        return response

class CheckEven:
    def __init__(self, get_response):
        print("initialized -->")
        self.get_response = get_response

    def __call__(self, request):
        print("start -->")
        number = request.POST.get("number")
        if number and int(number)%2:
            return JsonResponse({"messge":"Failed from the middleware!"})
        request.POST = {'data':number}
        response = self.get_response(request)
        print("end")
        return response
    
    # process view

    def process_view(request, view_func, *args, **kargs):
        print("procees view of CheckEven")
        return None
        # return JsonResponse({"message":"Returned from CheckEven"})


    # Exception     

    def process_exception(self, request, exception):
        print("Exception in CheckEven")
        msg = str(exception)
        return JsonResponse({"messsage":msg}, status = 400)

# ----------------------- E N D -----------------------------------------