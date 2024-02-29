from django.contrib import admin
from .models import CifUserDetail, ProductConfig
# Register your models here.

class CifUserDetailAdmin(admin.ModelAdmin):
    list_display = ('cif_id', 'external_id', 'email_id', 'mobile_number', 'pan_number' , 'date_of_birth' ,'profile_type', 'user_address', 'created_at','updated_at')
    # list_display_links = ('cif_id', 'external_id')
    list_per_page = 100
    # list_filter = ('profile_type',)
    search_fields = ('cif_id', 'external_id', 'email_id', 'mobile_number')

class ProductConfigAdmin(admin.ModelAdmin):
    list_display = ('product_id','version','config','created_at','updated_at')
    list_per_page = 100
    search_fields = ['product_id','version']

admin.site.register(CifUserDetail, CifUserDetailAdmin)
admin.site.register(ProductConfig, ProductConfigAdmin)