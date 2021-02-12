from django.contrib import admin
from .models import Partner, SocialNetwork, Category

# Register your models here.

admin.site.register(Partner)
admin.site.register(Category)
admin.site.register(SocialNetwork)