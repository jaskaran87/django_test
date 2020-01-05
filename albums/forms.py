from django import forms
from django.core.validators import RegexValidator

#from crispy_forms.helper import FormHelper
class ReporterForms (forms.Form):
    first_name = forms.CharField(
            widget = forms.TextInput(
                    attrs = {
                        "class" : "form-class",
                        "id" : "first_name",
                        "placeholder":"First Name", 
                    }
                )
        )
    last_name = forms.CharField(
            widget = forms.TextInput(
                    attrs = {
                        "class": "form-class", 
                        "id" : "last_name",
                        "placeholder" : "last_name",
                    }
                )
        )
    email = forms.EmailField(
            widget = forms.EmailInput(
                    attrs = {
                        'class' : "form-class",
                        'id' : 'email',
                        'placeholder' : 'email'
                    }
                )
        )


from .models import Reporter, Article
class ContactModel(forms.ModelForm):
    class Meta:
        model = Reporter
        fields = ('first_name','last_name','email')



class ArticleModel(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user','')
        super(ArticleModel, self).__init__(*args, **kwargs)
        self.fields['reporter'] = forms.ModelChoiceField(
                                                empty_label = 'Select',
                                                queryset = Reporter.objects.all()
                                            )

    headline = forms.CharField (
                                error_messages =  {
                                                    'Invaild':' headline dear', 
                                                    'required':"asdf"
                                                },
                                validators = [
                                  #  RegexValidator(r'^[0-9]+$', 'Enter a valid country calling code.'),
                                ] ,
                                label_suffix=' ='
                            )

    class Meta:
        model = Article
        fields = ('headline', 'pub_date', 'reporter')