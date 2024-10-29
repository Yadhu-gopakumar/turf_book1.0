
from django.urls import path
from . import views
urlpatterns = [
    path('turf',view=views.ownerhome,name='ownerhome',)

]
