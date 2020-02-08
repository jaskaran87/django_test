from django.urls import path
from .views import (
						CityAdd,
						PopulationSum
				)

urlpatterns = [
	path('', CityAdd.as_view(), name = 'CityAdd'),
	path('population', PopulationSum.as_view(), name="population")

]