from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.homepage, name='home'),
    path('result/', view=views.result_indiv, name='result'),
]