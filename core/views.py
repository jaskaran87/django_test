from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
import datetime
from .forms import ContactForms
# Create your views here.
def render_html(request):
    print(datetime.datetime.now())
    return HttpResponse("Hello World, Render Html")

def home(request):
    data = {'data' : [1,2,3,4,5,6]}
    return render(request, 'home.html', data)


def login(request):
    return render(request, 'home.html')
    

def contact_us(request):
    content_forms = ContactForms(request.POST or None)
    data = { 'content_forms': content_forms }
    # if request.method == "POST":
    #     print(request.POST)
    #     print(request.POST.get('email'))
    print(content_forms.errors.as_data())
    print(content_forms.is_valid())
    # print(content_forms.message)
    if content_forms.is_valid():
        print('here')
        print(content_forms.cleaned_data)

    return render(request, 'contact_us.html', data)

from .models import Product

class PorductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/list.html'
    def get_context_data(self, *args, **kwargs):
        context = super(PorductListView, self).get_context_data(*args, **kwargs)
        context['text'] = 'book'
        return context

class ProductSlugView(DetailView):
    template_name = "products/detail.html"

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        instance = get_object_or_404(Product, slug = slug, active = True)
        if instance is None:
            raise Http404 ('Product is not found 404')
        return instance

class ProductDetailView(DetailView):
    #   queryset = Product.objects.all()
    template_name = 'products/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get_object (self, *args, **kwargs):
        print(self.kwargs)
        request = self.request
        pk = self.kwargs.get('pk')
        print(pk)
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404('Product desen\'t exits')
        return instance 

class FeaturedProduct(ListView):
    template_name = 'products/list.html'

    def get_queryset(self, *args, **kwargs):
        return Product.objects.get_featured_products()