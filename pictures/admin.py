from django.contrib import admin

from .models import Picture

class ImageAdmin(admin.ModelAdmin):
     list_display = ('title', 'raiting', 'image_tag')

admin.site.register(Picture, ImageAdmin)

# Register your models here.
