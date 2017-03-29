import json
from django.http import HttpResponse
from django.core import serializers
from .models import Album


def index(request):
    albums = Album.objects.all()
    json_data = serializers.serialize('json', albums)
    return HttpResponse(json_data, content_type='application/json')
    #all_albums = Album.objects.all()
    #html = ''

    #for album in all_albums:
    #    url = '/music/'+ str(album.id) +'/'
    #    html += '<a href="'+url+'"> '+ album.album_title +' </a><br>'

    #return HttpResponse(html)


# def detail(request, album_id):
#     return HttpResponse("<h2>Details for Album id : "+ str(album_id)+"</h2>")
