from django.urls import path
from .views import  (   home, render_html, contact_us, 
                        PorductListView,  ProductDetailView, 
                        FeaturedProduct, ProductSlugView) 
urlpatterns = [
    path('', home, name="home"), 
    path('render_html/', render_html),
    path('contact_us/', contact_us),
    path('list/', PorductListView.as_view()),
    path('detail/<int:pk>/', ProductDetailView.as_view()),
    path('featured/', FeaturedProduct.as_view()),
    path('slug/<slug:slug>/', ProductSlugView.as_view() , name="slug_name"),
]