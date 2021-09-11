from django.http import HttpResponse
import requests
import json

def index(request):
    return HttpResponse("Hello, world. You're at the death_table index.")

def get_data(request):
    start_date = input('Введи дату начала >>>')
    end_date = input('Введи дату конца >>>')
    r = requests.get('https://covidtrackerapi.bsg.ox.ac.uk/api/v2/stringency/date-range/{YYYY-MM-DD}/{YYYY-MM-DD}')
    r.json()