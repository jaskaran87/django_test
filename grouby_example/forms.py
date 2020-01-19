from django import forms
from .models import City
from country.models import Country

class CityForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CityForm, self).__init__(*args, **kwargs)
		self.fields['country'] = forms.ModelChoiceField(
										empty_label = 'Select',
										queryset = Country.objects.all()
									)
	class Meta:
		model = City
		fields = ('country', 'name', 'population')
