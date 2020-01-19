from django.shortcuts import (render, get_object_or_404, redirect)
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.views import View
from django.views.generic import ListView
from .forms import CountryFrom, StateFrom, CityFrom
from .models import Country, State, City

class CountryList(ListView):
    def get_template_names(self, *args, **kwargs):
      return ['albums/list.html']
    def get_queryset(self, *args, **kwargs):
      data = Country.objects.filter( 
                                state__is_active = True
                            ).filter(
                                state__city__is_active = True
                            ) .distinct()
      print (data.query)
      #Country.objects.filter(Exists(State.objects.filter(country_id=OuterRef('pk'), is_active=True)).filter(Exists(City.objects.filter(state__country_id=OuterRef('pk')), is_active=True))
      return data
    

class CountryAdd(View):
    def get(self, request, *args, **kwargs):
        Forms = CountryFrom()
        return render(request, 'albums/add.html', { 'Forms' : Forms })

    def post(self, request, *args, **kwargs):
        Forms = CountryFrom(request.POST or None)
        if Forms.is_valid():
            Forms.save()
            Forms = CountryFrom()
        return render(request, 'albums/add.html', { 'Forms' : Forms })


class StateAdd(View):
    def get(self, request, *args, **kwargs):
        Forms = StateFrom()
        return render(request, 'albums/add.html', {'Forms': Forms})
    
    def post(self, request, *args, **kwargs):
        Forms = StateFrom(request.POST or None)
        if Forms.is_valid():
            Forms.save()
            Forms = StateFrom()
        return render(request, 'albums/add.html', {'Forms': Forms})

class CityAdd(View):

    def get(self, request, *args, **kwargs):
        Forms = CityFrom( state_id = kwargs.get("id"))
        return render(request, 'albums/add.html', {'Forms': Forms})

    def post(self, request, *args, **kwargs): 
        Forms = CityFrom(request.POST or None , state_id = kwargs.get("id"))
        if Forms.is_valid():
            Forms.save()
            return redirect ('city' , id = kwargs.get("id"))
        return render(request, 'albums/add.html', {'Forms': Forms})