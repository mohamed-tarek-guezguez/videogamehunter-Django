from django.contrib import admin
from .models import Product, Contact, News, Story, Banner, Ytb

# Register your models here.
class searchAdmin(admin.ModelAdmin):
    search_fields = ('Title',)

admin.site.register(Product, searchAdmin)
admin.site.register(Contact)
admin.site.register(News)
admin.site.register(Story)
admin.site.register(Banner)
admin.site.register(Ytb)