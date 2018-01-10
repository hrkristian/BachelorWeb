from django.db import models

# Create your models here.
from organizer.models import Medlem

class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField(
    max_length=255,
    help_text='A label for URL config.',
    unique_for_month='pub date'
    )
    text = models.TextField()
    date = models.DateField('date published', auto_now_add=True)
    medlem = models.ManyToManyField(Medlem, related_name='dagbok_posts')
    class Meta:
        verbose_name = 'dagbok post'
        ordering = ['-date']
        get_latest_by = 'date'
