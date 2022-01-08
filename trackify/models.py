from django.db import models

from trackify.validators import file_size

# Create your models here.

class audio(models.Model):
    caption=models.CharField(max_length=100)
    audio = models.FileField(upload_to="audio/%y", validators=[file_size])
    def __str__(self):
        return self.caption