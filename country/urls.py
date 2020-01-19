from django.urls import path
from .views import *

urlpatterns = [
	path('', CountryAdd.as_view(), name = "country"),
	path('state/', StateAdd.as_view(), name = "state"),
	path('state/city/<int:id>/', CityAdd.as_view(), name="city"),
	path('list/', CountryList.as_view(), name="list")
]