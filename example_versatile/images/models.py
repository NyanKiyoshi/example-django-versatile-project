from django.db import models
from versatileimagefield.fields import VersatileImageField


class ExampleModel(models.Model):
    image = VersatileImageField(
        'Image',
        upload_to='images/'
    )
