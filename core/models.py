from django.db import models
import random, os
# Create your models here.
from django.db.models.signals import pre_save, post_save
 
from .utils import unique_slug_generator
from django.urls import reverse


def get_filename_ext(filename):
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(filename)
    return name, ext

def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1,33339999999)
    name, ext = get_filename_ext(filename)
    print(name, ext)
    final_filename = '{new_filename}{ext}'.format(
                                            new_filename=new_filename, 
                                            ext=ext
                                        )
    return "core/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)

class ProductQuerySet(models.query.QuerySet):
    def featured(self):
        return self.filter(featured = True)
    def active(self):
        return self.filter(active = True)

class ProductManager(models.Manager):
    
    def get_queryset(self):
        return ProductQuerySet(self.model, using = self._db)
    
    def all(self):
        return self.get_queryset().active()
    
    def featured(self):
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id = id)
        if qs.count() == 1:
            return qs.first()
        return None

    
    def get_featured_products(self):
        qs = self.get_queryset().filter(featured = True)
        if qs.count() > 0:
            return qs.all()
        return None

class Product(models.Model):
    title = models.CharField(max_length = 120)
    description = models.TextField()
    slug = models.SlugField(blank = True)
    price = models.DecimalField(
                decimal_places = 2,
                max_digits = 20,
                default = 39.99 
            )
    #image = models.FileField(upload_to = upload_image_path, null = True, blank =True)
    image = models.ImageField(upload_to = upload_image_path, null = True, blank = True)
    featured = models.BooleanField(default = False)
    active = models.BooleanField(default = True)
    objects = ProductManager()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def slug_url(self):
        return '/products/slug/{slug}'.format(slug = self.slug)

    def slug_reverse_url(self):
        return reverse('products:slug_name', kwargs = {'slug': self.slug})

def product_pre_save_receiver(sender,instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender = Product)