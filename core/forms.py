from django import forms

class ContactForms (forms.Form):
	fullname = forms.CharField(
		widget = forms.TextInput(
			attrs = {
					"class": "form-control", 
					"id" :"form_full_name", 
					"placeholder":"Your name"
				}
		)
	)
	email = forms.EmailField(
		widget = forms.EmailInput(
			attrs = {
				'class' : "form-control",
				'id': "email",
				'placeholder' : 'Email' 
			}
		)
	)
	content = forms.CharField(
		widget = forms.Textarea(
			attrs = {
				"class": "form-control",
				"id" : "content",
				 
			}
		)
	)
