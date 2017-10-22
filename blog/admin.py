from django.contrib import admin
from .import models
#from django_ModelAdmin.admin import ModelAdmin
class PostAdmin(admin.ModelAdmin):
    list_display = ("title","created_date")
    prepopulated_fields={"slug":("title",)}

admin.site.register(models.Post,PostAdmin)
