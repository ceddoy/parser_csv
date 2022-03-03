from django.contrib import admin

from parserapp.models import CSV_file, Item

admin.site.register(Item)
admin.site.register(CSV_file)
