from django.http import HttpResponse
from django.shortcuts import  render
from death_table.models import Data
import requests

def index(request):
    return HttpResponse("Hello, world. You're at the death_table index.")

def get_data(request):
    all_data = {}
    if 'country_code' in request.GET:
        country_code = request.GET['country_code']
        url = 'https://covidtrackerapi.bsg.ox.ac.uk/api/v2/stringency/date-range/2021-09-01/2021-09-02'
        response = requests.get(url)
        res = response.json()
        data = res['data']

        for i in data:
            country_data = Data(
                date_value = i['date_value'],
                country_code = i['country_code'],
                confirmed = i['confirmed'],
                deaths = i['deaths'],
                stringency_actual = i['stringency_actual'],
                stringency = i['stringency']
            )
            country_data.save()
            all_data = Data.objects.all().order_by('-deaths')
        
    return render (request, 'meals/meal.html', { "all_data":all_data} )


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