from django.urls import path
from .views import (
						CityAdd,
				)

urlpatterns = [
	path('', CityAdd.as_view(), name = 'CityAdd'),
]