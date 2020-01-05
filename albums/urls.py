from django.urls import path
from . import views

#article

urlpatterns = [
    path('add/', views.add),
    path('add_model/', views.model_add),
    path('article_add/', views.article_add),
    path('class/', views.add_form.as_view() , name = 'class'),
]
 