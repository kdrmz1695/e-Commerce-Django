from django.contrib import admin
from .models import Categories, Brands, Products,Tags, Variations
# Register your models here.



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'seo_title', 'seo_description', 'slug', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name', 'seo_title', 'seo_description', 'slug']

admin.site.register(Categories, CategoryAdmin) # At this part, added CategoryAdmin. Firstly, added Categories. This is
# model and CategoryAdmin is Category's class.

class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'seo_title', 'description', 'slug', 'is_active', 'image']
    list_filter = ['is_active']
    search_fields = ['name', 'seo_title', 'seo_description', 'slug']
admin.site.register(Brands,BrandAdmin)

class InlineVariations(admin.StackedInline):
    model = Variations
    extra = 1
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'price', 'category', 'discounted_price', 'is_active', 'image','date']
    list_filter = ['is_active']
    search_fields = ['name', 'seo_title', 'seo_description', 'slug','price','discounted_price','user']
    inlines= [InlineVariations]

admin.site.register(Products,ProductAdmin)
admin.site.register(Tags)

