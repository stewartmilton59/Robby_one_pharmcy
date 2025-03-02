from django.contrib import admin
from .models import Branch

admin.site.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('location', 'description')
