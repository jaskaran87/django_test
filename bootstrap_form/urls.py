from django.urls import path

# bootstrap_form/form
# namespace = "boot_form"
from . import views
urlpatterns = [
	path('form/', views.form, name = "form"),
	path('form_edit/<int:pk>', views.form_edit, name = "form_edit"),
	path('form_delete/<int:pk>', views.form_delete, name = "form_delete")
]