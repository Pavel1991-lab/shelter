from dogs.models import Dog, Category
from django.contrib import admin



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', )





@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', )
    list_filter = ('category', )









