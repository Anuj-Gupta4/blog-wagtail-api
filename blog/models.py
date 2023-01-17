from django.db import models

# Create your models here.
# blog/models.py
from wagtail.embeds.blocks import EmbedBlock
from wagtail.api import APIField
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from rest_framework.fields import DateField, CharField
from wagtail.images.api.fields import ImageRenditionField

class BlogPageAuthor(Orderable):
    page = models.ForeignKey('blog.BlogPage', on_delete=models.CASCADE, related_name='authors')
    name = models.CharField(max_length=255)

    api_fields = [
        APIField('name'),
    ]


class BlogPage(Page):
    published_date = models.DateTimeField()
    embed = EmbedBlock(max_width=800, max_height=400)
    body = RichTextField()
    feed_image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, null=True)
    private_field = models.CharField(max_length=255)

    # Export fields over the API
    api_fields = [
        # Change the format of the published_date field to "Thursday 06 April 2017"
        APIField('published_date', serializer=DateField(format='%A %d %B %Y')),
        APIField('embed', serializer=CharField()),
        APIField('body', serializer=CharField()),
        APIField('feed_image_thumbnail', serializer=ImageRenditionField('fill-100x100', source='feed_image')),
        APIField('authors', serializer=CharField()),  # This will nest the relevant BlogPageAuthor objects in the API response
    ]