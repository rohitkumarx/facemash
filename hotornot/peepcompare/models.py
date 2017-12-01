from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FaceMash(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name='Superuser')
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="facemash_photos")
    ratings = models.FloatField(default=100)

    class Meta:
        verbose_name_plural = 'Facemash'

    def __unicode__(self):
        return self.name

#9f7388