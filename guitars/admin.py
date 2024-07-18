from django.contrib import admin
from .models import Brand, Model, Guitar, ImagesGuitar
# Register your models here.

class ModelInline(admin.StackedInline):
    model = Model
    extra = 2
    
class ImageGuitarInline(admin.TabularInline):
    model = ImagesGuitar
    extra = 3

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    
    fieldsets = (
        ('Information', {
            "fields": (
                'name_company',
            ),
        }),
        ('Contact Information', {
            "classes": ('collapse',),
            "fields": (
                'website_address', 'origin'        
            ),
        }),
    )
    
    inlines = [
        ModelInline,
    ]
    
    list_display = ('id_brand', 'name_company', 'website_address', 'origin')
    
    list_display_links = ('id_brand','name_company')
    list_editable = ('website_address',)
#    inlines
    list_filter = ('origin',)
    search_fields = ('name_company','origin')
# 
#admin.site.register(Brand, BrandAdmin)

class GuitarAdmin(admin.ModelAdmin):
    inlines = [ImageGuitarInline,]

admin.site.register(Guitar, GuitarAdmin)
admin.site.register(Model)