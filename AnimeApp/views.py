from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from AnimeApp.models import Topicinfo
from AnimeApp.serializers import TopicinfoSerializer

from django.core.files.storage import default_storage

import requests,json

from .forms import Topic_form


# Create your views here.
def ok(request):
    return render(request,"ok.html")

@csrf_exempt
def home(request):
    #form=Topic_form(request.POST or None)
    letter=Topicinfo()


    response=requests.get("https://animechan.vercel.app/api/random").json()
    
    L=[]
    for i in response.values():
        L.append(i)
    import sqlite3

    L4=""

    if L[0][0] in ["A","B","C","D","E","F","G",1,2,3,4,5,6,7,8,9,0]:
        L4="Comedy"
    elif L[0][0] in ["H","I","J","K","L","M","N","O","P"]:
        L4="Action"
    else:
        L4="Adventure"

    conn=sqlite3.connect("Anime_backend.db")
    c=conn.cursor()

    def create_table():
        c.execute('CREATE TABLE IF NOT EXISTS mytable_main(Anime TEXT,Character TEXT, Quote TEXT,Category TEXT)')

    def data_entry():
        c.execute("INSERT INTO mytable_main(Anime, Character,Quote,Category) values(?,?,?,?)",(L[0],L[1],L[2],L4))
        conn.commit()
        conn.close()

    create_table()
    data_entry()

    
    


    return render(request,"home.html",{"response":response})
    
    