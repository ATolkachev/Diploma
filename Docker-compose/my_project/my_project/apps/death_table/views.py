from django.http import HttpResponse
from django.shortcuts import render
import requests
import json

def index(request):
    return HttpResponse("Hello, world. You're at the death_table index!!!!.")

def get_data(request):
    start_date = input('Введи дату начала >>>')
    end_date = input('Введи дату конца >>>')
    r = requests.get('https://covidtrackerapi.bsg.ox.ac.uk/api/v2/stringency/date-range/{YYYY-MM-DD}/{YYYY-MM-DD}')
    r.json()



# from django.shortcuts import  render
# from meal_app.models import Meal
# import requests

# def get_meals(request):
#     all_meals = {}
#     if 'name' in request.GET:
#         name = request.GET['name']
#         url = 
#         'https://www.themealdb.com/api/json/v1/1/search.php? 
#         s=%s' % name
#         response = requests.get(url)
#         data = response.json()
#         meals = data['meals']

#         for i in meals:
#             meal_data = Meal(
#                 name = i['strMeal'],
#                 category = i['strCategory'],
#                 instructions = i['strInstructions'],
#                 region = i['strArea'],
#                 slug = i['idMeal'],
#                 image_url = i['strMealThumb']
#             )
#             meal_data.save()
#             all_meals = Meal.objects.all().order_by('-id')

#     return render (request, 'meals/meal.html', { "all_meals": 
#     all_meals} )



def meal_detail(request, id):
    meal = Meal.objects.get(id = id)
    print(meal)
    return render (
        request,
        'meals/meal_detail.html',
        {'meal': meal}
    )