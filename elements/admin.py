from django.contrib import admin
from .models import Element, Category, Type, Product, User

admin.site.register(Element)
admin.site.register(Category)
admin.site.register(Type)
admin.site.register(Product)
admin.site.register(User)