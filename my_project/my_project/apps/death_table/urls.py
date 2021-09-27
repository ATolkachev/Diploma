from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('', include ('meal_app.urls'))
    path('death_table', views.get_data, name = "get_data"),
    #path('meals/<int:id>/',views.meal_detail, name = "meal_detail")
]