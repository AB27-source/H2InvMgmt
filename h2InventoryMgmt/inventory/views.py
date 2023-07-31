from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Beverage

# Create your views here.

def index(request):
    beverage_list = Beverage.objects.order_by('name')  # Order by the 'name' field
    context = {
        "beverage_list": beverage_list
    }

    return render(request, "inventory/index.html", context)

def detail(request, beverage_id):
    beverage = get_object_or_404(Beverage, pk=beverage_id)
    return render(request, "polls/detail.html", {"beverage": beverage})
