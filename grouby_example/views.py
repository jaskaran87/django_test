from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .forms import CityForm
from django.db.models import (Sum, Avg)
from .models import City

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


class PopulationSum(ListView):
    def get_queryset(self, *args, **kwargs):
        return City.objects.values('country__name') \
                    .annotate(country__population = Sum('population')) \
                    .order_by('-country__population')
    def get_template_names(self, *args, **kwargs):
        return ['group_by/list.html']
    