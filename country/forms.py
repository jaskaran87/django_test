from django import forms
from django.core.validators import RegexValidator
from .models import Country, State, City
class CountryFrom(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CountryFrom,self).__init__(*args, **kwargs)

    class Meta:
        model = Country
        fields = ('name',)

class StateFrom(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StateFrom,self).__init__(*args, **kwargs)
        self.fields['country'] = forms.ModelChoiceField(
                                    empty_label = 'Select',
                                    queryset = Country.objects.all()

                                )
    class Meta:
        model = State
        fields = ('country', 'name')

class CityFrom(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.state_id = kwargs.pop('state_id', None)
         
        super(CityFrom,self).__init__(*args, **kwargs)
        self.fields['state'] = forms.ModelChoiceField(
                                 empty_label = 'Select',
                                 queryset = State.objects.filter(country = self.state_id ).all()
                                ) 
    class Meta:
        model = City
        fields = ('state', 'name')