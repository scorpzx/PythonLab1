from django.db import models
from django.utils.safestring import mark_safe

class Picture(models.Model):
    title = models.CharField(max_length = 250)
    image = models.ImageField(upload_to='images/')
    raiting = models.IntegerField(default = 0)


    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="height:100px;" />' % self.image.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

    def __str__(self):
        return self.title

