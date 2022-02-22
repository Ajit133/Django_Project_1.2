from django.contrib import admin
from second_app.models import Musician,Album

# Register your models here.
admin.site.register(Musician)
admin.site.register(Album)