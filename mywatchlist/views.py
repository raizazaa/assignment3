from django.shortcuts import render
from mywatchlist.models import ItemMyWatchList
from django.http import HttpResponse
from django.core import serializers

def show_mywatchlist(request):
    data_mywatchlist_item = ItemMyWatchList.objects.all()
    context = {
        'mywatchlist_list': data_mywatchlist_item,
        'name': 'Raizaz Achmad Asyraf',
        'student_id': '2106657815'
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = ItemMyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = ItemMyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")