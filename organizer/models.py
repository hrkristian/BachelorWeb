from django.db import models
from django.urls import reverse

# Create your models here.
class Medlem(models.Model):
    name = models.CharField(max_length=63, db_index=True)
    slug = models.SlugField(
    max_length=31,
    unique=True,
    help_text='A label for URL config.'
    )
    contact = models.EmailField()

    def get_absolute_url(self):
        return reverse('dagbok', kwargs={'slug':self.slug})
    def get_create_url(self):
        return reverse('dagbok_post_create', kwargs={'slug':self.slug})

    class Meta:
        ordering = ['name']
