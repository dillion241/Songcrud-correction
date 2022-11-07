from django.shortcuts import render
from django.http import HttpResponse
from .models import Artiste, Song, Lyrics
from .serializers import ArtisteSerializer, SongSerializer, LyricsSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser

# Create your views here.

def Artiste_list (request):

    if request.method == 'GET':
        artiste = Artiste.objects.all()
        serializer = ArtisteSerializer(artiste, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArtisteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

        