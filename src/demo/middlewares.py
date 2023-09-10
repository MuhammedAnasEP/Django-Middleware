from django.http import JsonResponse

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