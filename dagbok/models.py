from django.db import models
from django.shortcuts import reverse
# Create your models here.
from organizer.models import Medlem

class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField(
    max_length=255,
    help_text='A label for URL config.',
    unique_for_date='date'
    )
    text = models.TextField()
    date = models.DateField('date published', auto_now_add=False)
    medlem = models.ForeignKey(Medlem, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('dagbok', kwargs={'slug':self.slug})
    def get_create_url(self):
        return reverse('dagbok_post_create', kwargs={'slug':self.slug})
    def get_edit_url(self):
        return reverse('dagbok_post_edit', kwargs={
            'slug':self.slug,
            'year':self.date.year,
            'month':self.date.month,
            'day':self.date.day})
    def get_delete_url(self):
        return reverse('dagbok_post_delete', kwargs={
            'slug':self.slug,
            'year':self.date.year,
            'month':self.date.month,
            'day':self.date.day})
    class Meta:
        verbose_name = 'dagbok post'
        ordering = ['-date']
        get_latest_by = 'date'
