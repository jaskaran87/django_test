from django.shortcuts import render
from django.views import View

from .forms import CityForm

class CityAdd(View):
	def get(self, request, *args, **kwargs):
		Forms = CityForm() 
		return render( 
						request, 
						'albums/add.html', 
						{
							'Forms' : Forms
						} 
					)


	def post(self, request, *args, **kwargs):
		Forms = CityForm(request.POST or None)
		if Forms.is_valid():
			Forms.save()
			Forms = CityForm()
		return render(request, 'albums/add.html', { 'Forms' : Forms })