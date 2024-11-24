from django.http import JsonResponse

def hello_world_json(request):
    return JsonResponse({"Message": "Hello World!"})
