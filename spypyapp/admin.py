from django.contrib import admin
from .models import Profile, Neighbor, Business

# Register your models here.
admin.site.register(Neighbor)
admin.site.register(Profile)
admin.site.register(Business)