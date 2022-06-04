from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Hoppers

class HoppersAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

# Register your models here.

admin.site.register(Hoppers, HoppersAdmin)
