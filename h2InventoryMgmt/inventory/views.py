from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("You're at the inventory index.")