from django.contrib import admin

# Register your models here.
from .models import WordModel
admin.site.register(WordModel)