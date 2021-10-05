from django.db import models
from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField

from ckeditor.fields import RichTextField

# Create your models here.

class Kost(models.Model):
    id = models.AutoField(primary_key=True)
    image = CloudinaryField('image', null=True)
    title = models.CharField(max_length=200, null=True)
    caption = RichTextField(null=True)

    class Meta:
        ordering = ['-id',]

    def save(self, *args, **kwargs):
        super(Kost, self).save(*args, **kwargs)
        return self.id
        super().save()

    def __str__(self):
        return "{}".format(self.title)