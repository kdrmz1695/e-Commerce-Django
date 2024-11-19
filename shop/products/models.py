from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Categories(models.Model):  #how to create model
    name=models.CharField(max_length=155)
    upper_category=models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True,
                                   help_text="If this category related with another category please fill in here.")
    seo_title=models.CharField(max_length=155, blank=True, null=True)
    seo_description=models.TextField(blank=True, null=True)
    slug=models.SlugField(max_length=155, unique=True, blank=True, null=True) #url must be unique. Slug Example:
    # Haci Sakir Soap>  haci-sakir-soap-124324234(this id is unique)
    is_active=models.BooleanField(default=True)
#the sub category's parameters: self= works for its own class. on_delete= if main category deleted other sub
    # categories will be deleted. blank= it can be blank. null= in database can be blank.

    #######NOTE: when model has any changes we have to do migration on terminal. Otherwise it won't work. ########


    class Meta:   #Works for models' name looks plural or single.
        verbose_name_plural="Categories"
        verbose_name="Category"

# how object looks on screen. Used __str__ func.

    def __str__(self):          #self works for its own class
        return self.name

class Brands(models.Model):
    name=models.CharField(max_length=155)
    description=models.TextField(blank=True,null=True)
    seo_title=models.CharField(max_length=155,blank=True,null=True)
    seo_description=models.TextField(blank=True, null=True)
    slug=models.SlugField(max_length=155,unique=True,null=True,blank=True)
    is_active=models.BooleanField(default=True)
    image=models.ImageField(upload_to="brand_pictures",blank=True,null=True)

    class Meta:   #Works for models' name looks plural or single.
        verbose_name_plural="Brands"
        verbose_name="Brand"

    def __str__(self):
        return self.name

class Tags(models.Model):
    name=models.CharField(max_length=155)
    slug=models.SlugField(max_length=155,blank=True,null=True)
    is_active=models.BooleanField(default=True)

    class Meta:
        verbose_name_plural='Tags'
        verbose_name='Tag'
    def __str__(self):
        return self.name

class Products(models.Model):
    name=models.CharField(max_length=155,)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brands,on_delete=models.CASCADE)
    category=models.ForeignKey(Categories,on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price=models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    short_description=models.TextField(blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    seo_title=models.TextField(blank=True,null=True)
    seo_description=models.TextField(blank=True,null=True)
    slug=models.SlugField(blank=True,null=True)
    is_active=models.BooleanField(default=True)
    image=models.ImageField(upload_to='', blank=True,null=True)
    date=models.DateTimeField(auto_now=True)
    tags=models.ManyToManyField(Tags, blank=True)


    class Meta:
        verbose_name_plural="Products"
        verbose_name="Product"
    def __str__(self):
        return self.name


